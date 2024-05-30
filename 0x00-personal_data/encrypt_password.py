#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    function that expects one string argument name password
    and returns a salted, hashed password
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14))
    return hashed
