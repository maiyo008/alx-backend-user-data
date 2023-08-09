#!/usr/bin/env python3
"""
Manages basic authentication
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """
    Basic authentication class
    """
    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """
        Returns Base64 part of the authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        """
        Decodes Base64 authorization header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except base64.binascii.Error:
            return None
        except UnicodeDecodeError:
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Return the user email and password
        from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        decoded_header = decoded_base64_authorization_header.split(':')
        return decoded_header[0], decoded_header[1]

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
    ) -> TypeVar('User'):
        """
        Return user instance based on their email & password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        user = User.search({'email': user_email})
        if not user or not user[0].is_valid_password(user_pwd):
            return None
        return user[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Overloads Auth and retreives User instance of a request
        """
        if request is None:
            return None
        header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(header)
        if base64_header is None:
            return None
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_credentials = self.extract_user_credentials(decoded_header)
        if user_credentials is None:
            return None
        user_email, user_pwd = user_credentials
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
