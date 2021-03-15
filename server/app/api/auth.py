from flask import g, request, redirect, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity, verify_jwt_in_request,
    create_refresh_token
)
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from bson import ObjectId

from app.decorators import login_required
from app.utils import get_timestamp
from app.auth import get_user_by_id, get_user
from app.db import get_db, Groups
from . import bp


@bp.route('/auth/login', methods=['POST'])
def login():
    """ Route to login user
    """

    if not request.is_json:
        return jsonify({'success': False, 'message': "Missing JSON in request"}), 400

    data = request.json

    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    if (not username and not email) or not password:
        return jsonify({'success': False, 'message': "Missing email/username or password in parameters"}), 400

    user = get_user({
        'username': username,
        'email': email
    })

    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 401

    if not check_password_hash(user['password'], password):
        return jsonify({'success': False, 'message': 'Bad username or password'}), 401

    token_identity = {
        '_id': user['_id'],
        'groups': user.get('groups', [Groups.USER]),
        'created_at': get_timestamp()
    }

    access_token = create_access_token(identity=token_identity)
    refresh_token = create_refresh_token(identity=token_identity)

    return jsonify({
        'token': access_token,
        'user': {
            'id': str(user['_id']),
            'nickname': user.get('nickname', user['username']),
            'groups': user.get('groups', [Groups.USER]),
            'registered': user.get('registered')
        },
        'refresh_token': refresh_token,
        'success': True
    }), 200


@bp.route("/auth/refresh", methods=['GET'])
@jwt_required(refresh=True)
def refresh():
    """ Route to refresh user authentication token
    """

    token_identity = get_jwt_identity()

    user_id = token_identity.get('_id')
    if user_id is None:
        return jsonify({
            'token': '',
            'user': {},
            'success': False
        }), 200

    user = get_user_by_id(ObjectId(user_id))

    if not user:
        return jsonify({
            'token': '',
            'user': {},
            'success': False
        }), 200

    return jsonify({
        'token': create_access_token(identity=token_identity),
        'user': {
            'id': str(user['_id']),
            'nickname': user.get('nickname', user['username']),
            'groups': user.get('groups', [Groups.USER]),
        },
        'success': True
    }), 200


@bp.before_app_request
def load_logged_in_user():
    """ Set logged in user as g.user
    """

    try:
        verify_jwt_in_request()
    except Exception:
        g.user = None
        return

    token_identity = get_jwt_identity()

    if not token_identity:
        g.user = None
        return

    user_id = token_identity.get('_id')

    if user_id is None:
        g.user = None
        return

    g.user = get_user_by_id(ObjectId(user_id))
