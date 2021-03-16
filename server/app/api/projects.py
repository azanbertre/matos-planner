from flask import g, request, jsonify

from app.db import get_db, Groups
from app.auth import current_user
from app.decorators import login_required
from app.utils import get_timestamp
from app.models.Fortnight import Fortnight

from bson import ObjectId

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
            'fortnight_start': start,
            'fortnight_end': end,
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
        'fortnight_start': start,
        'fortnight_end': end,
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

    now = datetime.utcnow()

    last_year = now.replace(year=now.year - 1)

    date_1 = last_year.replace(month=12, day=1, hour=0, minute=0, second=0, microsecond=0)
    date_2 = date_1.replace(day=15)

    months = Fortnight.months

    fortnights = [
        {
            'name': Fortnight.get_slug(date_1),
            'value': date_1
        },
        {
            'name': Fortnight.get_slug(date_2),
            'value': date_2
        }
    ]

    date_1 = date_1.replace(month=1, year=date_1.year + 1)
    date_2 = date_2.replace(month=1, year=date_1.year)

    for m in months:

        fortnights.append({
            'name': Fortnight.get_slug(date_1),
            'value': date_1
        })

        fortnights.append({
            'name': Fortnight.get_slug(date_2),
            'value': date_2
        })

        if date_1.month < 12:
            date_1 = date_1.replace(month=date_1.month + 1)
            date_2 = date_2.replace(month=date_1.month)

    return jsonify({
        'success': True,
        'message': '',
        'fortnights': fortnights
    })

