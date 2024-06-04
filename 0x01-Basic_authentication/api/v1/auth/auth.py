#!/usr/bin/env python3
"""
necessary imports
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    The auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        another function
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path.endswith('/'):
            path = path[:-1]
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user function
        """
        return None
