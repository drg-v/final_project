from functools import wraps
from flask import jsonify, request, current_app
import jwt
from models.models import User
import datetime


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'missing authentication token'})
        try:
            data = jwt.decode(token[7:], current_app.config['SECRET_KEY'], algorithms="HS256")
            current_user = User.query.filter_by(id_=data['id']).first()
            if not current_user:
                return jsonify({'message': 'token is invalid'})
        except:
            return jsonify({'message': 'token is invalid'})
        return f(*args, **kwargs)

    return decorator


def generate_token(user_id, is_admin):
    return jwt.encode(
        {'id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30), 'adm': is_admin},
        current_app.config['SECRET_KEY'], algorithm="HS256")


def admin_token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'missing authentication token'})
        try:
            data = jwt.decode(token[7:], current_app.config['SECRET_KEY'], algorithms=["HS256"])
            if not data['adm']:
                return jsonify({'message': 'token is invalid'})
            current_user = User.query.filter_by(id_=data['id']).first()
            if not current_user or not current_user.is_admin:
                return jsonify({'message': 'token is invalid'})
        except:
            return jsonify({'message': 'token is invalid'})
        return f(*args, **kwargs)

    return decorator
