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

    def destroy_session(self, user_id: int) -> None:
        """
        The method updates the corresponding user’s session ID to None.
        """
        if user_id is None:
            return None
        try:
            self._db.update_user(user_id=user_id, session_id=None)
            return None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        implement the Auth.get_reset_password_token method.
        It take an email string argument and returns a string.
        """
        try:
            user = self._db.find_user_by(email=email)
            uuid = _generate_uuid()
            self._db.update_user(user.id, reset_token=uuid)
            return uuid
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        implement the Auth.update_password method. It takes reset_token
        string argument and a password string argument and returns None.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password).decode('utf-8')
            self._db.update_user(
                user.id, hashed_password=hashed_password, reset_token=None
                )
        except NoResultFound:
            raise ValueError
