#!/usr/bin/env python3
"""
DB Module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError


from user import Base, User


class DB:
    """
    DB class
    """
    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str):
        """
        Add user
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs):
        """
        Find user
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("No user found for the given criteria")
            return user
        except NoResultFound as e:
            raise e
        except InvalidRequestError as e:
            raise e

    def update_user(self, user_id: str, **kwargs) -> None:
        """
        Update user
        """
        allowed_attr = [
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
        ]
        try:
            user = self.find_user_by(id=user_id)
            for attr, value in kwargs.items():
                if attr not in allowed_attr:
                    raise ValueError("Invalid attribute: {}", attr)
                setattr(user, attr, value)
            self._session.commit()
        except NoResultFound:
            return None
        except InvalidRequestError:
            self._session.rollback()
