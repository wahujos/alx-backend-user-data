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
        # if path.endswith('/'):
        #     path = path[:-1]
        if not path.endswith('/'):
            path += '/'
        for excluded_path in excluded_paths:
            # if excluded_path.endswith('/'):
            #     excluded_path = excluded_path[:-1]
            if excluded_path.endswith('/'):
                excluded_path += '/'
            # if excluded_path.endswith('*'):
            #     if path.startswith(excluded_path[:1]):
            #         return False
            #     else:
            #         if path == excluded_path:
            #             return False
            if path == excluded_path:
                return False
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header
        """
        if request is None:
            return None
        # if 'Authorization' not in request.headers:
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')
        # return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user function
        """
        return None
