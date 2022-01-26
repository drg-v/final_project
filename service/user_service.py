"""
Module containing functions to work with User model

Functions:
    get_all_users() -> List[User]
    get_user(name: str) -> User
    login_user(name: str, password: str) -> tuple
    create_user(username: str, password: str) -> str
    block_user(user_id: int) -> str
    add_user_subscription(user_id: int) -> str
"""

from typing import List
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from models.models import User
from utils import generate_token


def get_all_users() -> List[User]:
    """Returns all users from the database"""

    return User.query.all()


def get_user(name: str) -> User:
    """Returns the user with appropriate username form the database"""

    return User.query.filter_by(username=name).first()


def login_user(name: str, password: str) -> tuple:
    """
    Finds user with appropriate username and checks it`s password.
    If credentials are correct generates token.

    :param name: the user`s name
    :param password: the user`s password
    :return: tuple containing token and user entity
    """

    user = User.query.filter_by(username=name).first()
    if user and check_password_hash(user.password, password) and user.status == "active":
        return generate_token(user.id_, user.is_admin), user


def create_user(username: str, password: str) -> str:
    """
    Creates new user with appropriate username and password.

    :param username: the user`s username
    :param password: the user`s password
    :return: the status of creation attempt
    """

    user = User.query.filter_by(username=username).first()
    if not user:
        password = generate_password_hash(password, method='sha256')
        user = User(username=username,
                    password=password,
                    status='active',
                    is_subscriber=False,
                    trial_attempts=2,
                    is_admin=False)
        db.session.add(user)
        db.session.commit()
        return 'success'
    return 'fail'


def block_user(user_id: int) -> str:
    """Blocks the user with appropriate id_ if it exists"""

    user = User.query.filter_by(id_=user_id).first()
    if not user:
        return 'fail'
    user.status = 'blocked'
    db.session.commit()
    return 'success'


def add_user_subscription(user_id: int) -> str:
    """Subscribes the user with appropriate id_ if it exists"""

    user = User.query.filter_by(id_=user_id).first()
    if not user:
        return 'fail'
    user.is_subscriber = True
    db.session.commit()
    return 'success'
