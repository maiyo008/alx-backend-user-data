#!/usr/bin/env python3
"""
Manages basic authentication
"""
from api.v1.auth.auth import Auth
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
