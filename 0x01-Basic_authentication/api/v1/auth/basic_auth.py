#!/usr/bin/env python3
"""
Manages basic authentication
"""
from api.v1.auth.auth import Auth


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
