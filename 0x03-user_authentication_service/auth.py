#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password
    """
    pass_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(pass_bytes, salt)
    return hash


def _generate_uuid() -> str:
    """
    Generate UUIDs
    """
    id = str(uuid.uuid4())
    return id


class Auth:
    """
    Auth class to interact with the authentication database
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers the user to the database
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            added_user = self._db.add_user(email, hashed_pwd)
            return added_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates user password
        """
        try:
            user = self._db.find_user_by(email=email)
            pass_bytes = password.encode('utf-8')
            pass_check = bcrypt.checkpw(pass_bytes, user.hashed_password)
            return pass_check
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Fetches session id
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return
