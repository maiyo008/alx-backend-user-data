#!/usr/bin/env python3
"""
Manages session authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Manage session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session id for a user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        sessionID = uuid.uuid4()
        self.user_id_by_session_id[user_id] = sessionID
        return sessionID
