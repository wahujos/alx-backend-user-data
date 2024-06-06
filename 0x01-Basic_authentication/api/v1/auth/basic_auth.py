#!/usr/bin/env python3
"""necessary imports required for the code"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class inherits from auth implements the basic authentication"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        extract_base64_authorization_header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[len('Basic '):]
