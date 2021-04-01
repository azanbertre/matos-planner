from flask import g, request, jsonify

from app.db import get_db, Groups
from app.auth import current_user
from app.decorators import login_required
from app.utils import get_timestamp

from . import bp


@bp.route('/roles', methods=('GET',))
def roles():
    db = get_db()

    roles = db.roles.find({
        'active': {'$ne': False}
    })

    return jsonify({
        'success': True,
        'message': '',
        'roles': list(roles)
    })


@bp.route('/roles', methods=('POST',))
@login_required
def post_roles():
    db = get_db()

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


@bp.route('/roles/<objectid:role_id>', methods=('PUT',))
@login_required
def roles_edit(role_id):
    db = get_db()

    data = request.json

    if not role_id:
        return jsonify({
            'success': False,
            'message': 'Não foi possivel editar o cargo'
        })

    name = data.get('name')
    capacity = data.get('capacity')

    query = {
        'name': name,
        'capacity': capacity,
        'edited_at': get_timestamp()
    }

    # filter null updates
    query = {k: query[k] for k in query if query[k] is not None}

    db.roles.update_one({'_id': role_id}, {
        '$set': query
    })

    return jsonify({
        'success': True,
        'message': 'Cargo editado com sucesso'
    })


@bp.route('/roles/<objectid:role_id>', methods=('DELETE',))
@login_required
def roles_delete(role_id):
    db = get_db()

    if not role_id:
        return jsonify({
            'success': False,
            'message': 'Não foi possivel excluir o cargo'
        })

    db.roles.update_one({'_id': role_id}, {
        '$set': {
            'active': False,
            'deactivated_at': get_timestamp()
        }
    })

    return jsonify({
        'success': True,
        'message': 'Cargo excluido com sucesso'
    })
