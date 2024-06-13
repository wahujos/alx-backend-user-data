#!/usr/bin/env python3
"""
importing the necessary imports
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    method that takes in a password string arguments
    and returns bytes.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        initialization function
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register a user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        hash_password = _hash_password(password)
        user = self._db.add_user(email=email, hashed_password=hash_password)
        return user
