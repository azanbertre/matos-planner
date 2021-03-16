from flask import g, request, jsonify

from app.db import get_db, Groups
from app.auth import current_user
from app.decorators import login_required
from app.utils import get_timestamp

from . import bp


@bp.route('/roles', methods=('GET', 'POST'))
@login_required
def roles():
    db = get_db()

    if request.method == 'POST':

        data = request.json

        name = data.get('name')
        capacity = data.get('capacity', 1)

        query = {
            'name': name,
            'capacity': int(capacity),
            'active': True,
            'created_at': get_timestamp()
        }

        db.roles.insert_one(query)

        return jsonify({
            'success': False,
            'message': 'Cargo adicionado',
        })

    roles = db.roles.find({
        'active': {'$ne': False}
    })

    return jsonify({
        'success': True,
        'message': '',
        'roles': list(roles)
    })
