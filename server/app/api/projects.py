from flask import g, request, jsonify

from app.db import get_db, Groups
from app.auth import current_user
from app.decorators import login_required
from app.utils import get_timestamp
from app.models.Fortnight import Fortnight

from copy import deepcopy

from bson import ObjectId
from collections import defaultdict

from datetime import datetime, timedelta

from . import bp


@bp.route('/projects', methods=('GET', 'POST'))
@login_required
def projects():
    db = get_db()

    if request.method == 'POST':

        data = request.json

        name = data.get('name')
        typ = data.get('type')
        start = data.get('fortnight_start')
        end = data.get('fortnight_end')

        query = {
            'name': name,
            'type': typ,
            'fortnight_start': {
                'name': Fortnight.get_slug(start),
                'value': start
            },
            'fortnight_end': {
                'name': Fortnight.get_slug(end),
                'value': end
            },
            'active': True,
            'created_at': get_timestamp()
        }

        db.projects.insert_one(query)

        return jsonify({
            'success': True,
            'message': 'Projeto adicionado',
        })

    projects = db.projects.find({
        'active': {'$ne': False}
    })

    return jsonify({
        'success': True,
        'message': '',
        'projects': list(projects)
    })


@bp.route('/projects/schedule', methods=('GET',))
@login_required
def projects_schedule():
    db = get_db()

    fortnights = Fortnight.get()

    projects = db.projects.find({
        'active': {'$ne': False}
    })

    schedule = []

    for p in projects:
        schedule.append({
            'name': p['name'],
            'start': len([f for f in fortnights if str(f['value']) <= p['fortnight_start']['value']]) - 1,
            'end': len([f for f in fortnights if str(f['value']) <= p['fortnight_end']['value']]) - 1
        })

    return jsonify({
        'success': True,
        'message': '',
        'schedule': sorted(schedule, key=lambda x: x['start']),
    })


@bp.route('/projects/<objectid:project_id>', methods=('PUT',))
@login_required
def projects_edit(project_id):
    db = get_db()

    data = request.json

    if not project_id:
        return jsonify({
            'success': False,
            'message': 'Não foi possivel editar o projeto'
        })

    name = data.get('name')
    typ = data.get('type')
    start = data.get('fortnight_start')
    end = data.get('fortnight_end')

    query = {
        'name': name,
        'type': typ,
        'fortnight_start': {
            'name': Fortnight.get_slug(start),
            'value': start
        },
        'fortnight_end': {
            'name': Fortnight.get_slug(end),
            'value': end
        },
        'edited_at': get_timestamp()
    }

    # filter null updates
    query = {k: query[k] for k in query if query[k] is not None}

    db.projects.update_one({'_id': project_id}, {
        '$set': query
    })

    return jsonify({
        'success': True,
        'message': 'Projeto editado com sucesso'
    })


@bp.route('/projects/<objectid:project_id>', methods=('DELETE',))
@login_required
def projects_delete(project_id):
    db = get_db()

    if not project_id:
        return jsonify({
            'success': False,
            'message': 'Não foi possivel excluir o projeto'
        })

    db.projects.update_one({'_id': project_id}, {
        '$set': {
            'active': False,
            'deactivated_at': get_timestamp()
        }
    })

    return jsonify({
        'success': True,
        'message': 'Projeto excluido com sucesso'
    })


@bp.route('/projects/fortnights', methods=('GET',))
# @login_required
def fortnights():

    fortnights = Fortnight.get()

    return jsonify({
        'success': True,
        'message': '',
        'fortnights': fortnights
    })

