#!/usr/bin/env python3
"""
importing the necessary imports
"""
import bcrypt
import uuid
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


def _generate_uuid() -> str:
    """
     The function should return a string representation of a new UUID
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """
         should expect email and password required arguments
         and return a boolean.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        check = bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        if check:
            return True
        return False

    def create_session(self, email: str) -> str:
        """
        It takes an email string argument and
        returns the session ID as a string.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        new_uuid = _generate_uuid()
        user.session_id = new_uuid
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        It takes a single session_id string
        argument and returns the corresponding User or None.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
