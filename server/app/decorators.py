from functools import wraps
from flask import g, jsonify, redirect, url_for, request

from app.auth import has_permission, has_group


def group_required(slug):
    def decorate_view(view):
        @wraps(view)
        def wrapped_view(**kwargs):
            if g.user is None:
                return jsonify({'success': False, 'message': 'You are not logged in.'}), 401
            if not has_group(g.user, slug):
                return jsonify({'success': False, 'message': 'Only {}s can access that.'.format(slug)}), 401
            return view(**kwargs)
        return wrapped_view
    return decorate_view


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            # TODO fix redirect
            return jsonify({'success': False, 'message': 'You are not logged in.'}), 401  # redirect(url_for('api.login'))
        return view(**kwargs)

    return wrapped_view


def permission_required(slug):
    def decorate_view(view):
        @wraps(view)
        def wrapped_view(**kwargs):
            if g.user is None:
                return jsonify({'success': False, 'message': 'You are not logged in.'}), 401
            if not has_permission(g.user, slug):
                return jsonify({'success': False, 'message': 'You do not have permission.'}), 401
            return view(**kwargs)
        return wrapped_view
    return decorate_view
