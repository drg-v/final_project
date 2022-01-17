from app import db
from models.models import User
from utils import generate_token
from werkzeug.security import generate_password_hash, check_password_hash


def get_all_users():
    return User.query.all()


def get_user(name):
    return User.query.filter_by(username=name).first()


def login_user(name, password):
    user = User.query.filter_by(username=name).first()
    if user and check_password_hash(user.password, password):
        return generate_token(user.id_, user.is_admin), user


def create_user(username, password):
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


def block_user(user_id):
    user = User.query.filter_by(id_=user_id).first()
    if not user:
        return 'fail'
    user.status = 'blocked'
    db.session.commit()
    return 'success'


def add_user_subscription(user_id):
    user = User.query.filter_by(id_=user_id).first()
    if not user:
        return 'fail'
    user.is_subscriber = True
    db.session.commit()
    return 'success'
