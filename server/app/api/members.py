from flask import g, request, jsonify

from app.db import get_db, Groups
from app.auth import current_user
from app.decorators import login_required
from app.utils import get_timestamp
from app.models.Fortnight import Fortnight

from bson import ObjectId

from . import bp


@bp.route('/members', methods=('GET', 'POST'))
@login_required
def members():
    db = get_db()

    if request.method == 'POST':

        data = request.json

        name = data.get('name')
        start = data.get('start')
        end = data.get('end')
        role_id = data.get('role_id')

        query = {
            'name': name,
            'fortnight_start': Fortnight.get_slug(start),
            'fortnight_end': Fortnight.get_slug(end),
            'role_id': ObjectId(role_id),
            'active': True,
            'created_at': get_timestamp()
        }

        db.members.insert_one(query)

        return jsonify({
            'success': True,
            'message': 'Membro adicionado',
        })

    members = db.members.aggregate([
        {
            '$match': {
                'active': {'$ne': True}
            }
        },
        {
            '$lookup': {
                'from': 'roles',
                'localField': 'role_id',
                'foreignField': '_id',
                'as': 'role'
            }
        }
    ])

    return jsonify({
        'success': True,
        'message': '',
        'members': list(members)
    })
