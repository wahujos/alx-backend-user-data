#!/usr/bin/env python3
"""
Iporting the necessary modules
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    authentication using sessions
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        instance method to create a session
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_Id = uuid4()
        self.user_id_by_session_id[session_Id] = user_id
        return session_Id
