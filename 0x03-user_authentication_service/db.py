#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
# Added some imports
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        method should save the user to the database.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwags) -> User:
        """
         returns the first row found in the users
         table as filtered by the method’s input arguments.
        """
        try:
            return self._session.query(User).filter_by(**kwags).one()
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        method that takes as argument a required usser_id
        integer and arbitrary keyword arguments, and returns None.
        """
        try:
            user_to_update = self.find_user_by(id=user_id)
        except NoResultFound:
            raise NoResultFound()
        for key, value in kwargs.items():
            if not hasattr(user_to_update, key):
                raise ValueError()
            setattr(user_to_update, key, value)
            self._session.commit()
            return None
