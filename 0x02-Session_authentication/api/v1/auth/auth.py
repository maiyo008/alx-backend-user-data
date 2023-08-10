#!/usr/bin/env python3
"""
Manage API authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """
    Manage
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        for p in excluded_paths:
            if p[:-1] == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        """
        if request is None:
            return None
        header_value = request.headers.get('Authorization')
        if not header_value:
            return None
        return header_value

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))
