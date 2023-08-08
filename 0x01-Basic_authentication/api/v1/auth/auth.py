#!/usr/bin/env python3
"""
Manage API authentication
"""
from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
