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
        start = data.get('fortnight_start')
        end = data.get('fortnight_end')
        role_id = data.get('role_id')
        capacity = data.get('capacity_override')

        query = {
            'name': name,
            'fortnight_start': {
                'name': Fortnight.get_slug(start),
                'value': start
            },
            'fortnight_end': {
                'name': Fortnight.get_slug(end),
                'value': end
            },
            'capacity_override': capacity,
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
                'active': {'$ne': False}
            }
        },
        {
            '$lookup': {
                'from': 'roles',
                'localField': 'role_id',
                'foreignField': '_id',
                'as': 'role'
            }
        },
        {
            '$unwind': '$role'
        }
    ])

    return jsonify({
        'success': True,
        'message': '',
        'members': list(members)
    })


@bp.route('/members/<objectid:member_id>', methods=('PUT',))
@login_required
def members_edit(member_id):
    db = get_db()

    data = request.json

    if not member_id:
        return jsonify({
            'success': False,
            'message': 'Não foi possivel editar o membro'
        })

    name = data.get('name')
    start = data.get('fortnight_start')
    end = data.get('fortnight_end')
    role_id = data.get('role_id')
    capacity = data.get('capacity_override')

    query = {
        'name': name,
        'fortnight_start': {
            'name': Fortnight.get_slug(start),
            'value': start
        },
        'fortnight_end': {
            'name': Fortnight.get_slug(end),
            'value': end
        },
        'capacity_override': capacity,
        'role_id': ObjectId(role_id) if role_id else None,
        'edited_at': get_timestamp()
    }

    # filter null updates
    query = {k: query[k] for k in query if query[k] is not None}

    db.members.update_one({'_id': member_id}, {
        '$set': query
    })

    return jsonify({
        'success': True,
        'message': 'Membro editado com sucesso'
    })


@bp.route('/members/<objectid:member_id>', methods=('DELETE',))
@login_required
def members_delete(member_id):
    db = get_db()

    if not member_id:
        return jsonify({
            'success': False,
            'message': 'Não foi possivel excluir o membro'
        })

    db.members.update_one({'_id': member_id}, {
        '$set': {
            'active': False,
            'deactivated_at': get_timestamp()
        }
    })

    return jsonify({
        'success': True,
        'message': 'Membro excluido com sucesso'
    })

