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


@bp.route('/capacity', methods=('GET',))
@login_required
def capacity():
    db = get_db()

    args = request.args

    typ = args.get('type')

    capacity = {
        'free': 0,
        'total': 0,
        'used': 0
    }

    projects = {p['_id']: p for p in db.projects.find({
        'active': {'$ne': False}
    }, {'fortnight_start': 1, 'fortnight_end': 1})}

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

    fortnights = {f['name']: {
        'value': f['value'],
        'capacity': deepcopy(capacity)
    } for f in Fortnight.get()}

    for m in members:
        member_capacity = int(m['role']['capacity'] if not m.get('capacity_override') else m['capacity_override'])

        for f in [f for f in Fortnight.get() if m['fortnight_start']['value'] <= str(f['value']) <= m['fortnight_end']['value']]:
            fortnights[f['name']]['capacity']['total'] += member_capacity

        for p_id in m.get('projects', []):
            if p_id not in projects:
                continue
            project = projects[p_id]

            for f in [f for f in Fortnight.get() if project['fortnight_start']['value'] <= str(f['value']) <= project['fortnight_end']['value']]:
                fortnights[f['name']]['capacity']['used'] += member_capacity

    fortnights = sorted([{
        'name': k,
        'value': fortnights[k]['value'],
        'capacity': {
            'total': fortnights[k]['capacity']['total'],
            'used': fortnights[k]['capacity']['used'],
            'free': fortnights[k]['capacity']['total'] - fortnights[k]['capacity']['used']
        }
    } for k in fortnights], key=lambda x: x['value'])

    now = datetime.utcnow()

    currency_capacity = [f for f in fortnights if is_current_fortnight(now, f['value'])][0]

    print([f for f in fortnights if is_current_fortnight(now, f['value'])])

    return jsonify({
        'success': True,
        'message': '',
        'capacity': fortnights,
        'currentCapacity': currency_capacity
    })


def is_current_fortnight(now, value):
    if now.month != value.month:
        return False

    if now < value:
        return False

    if now + timedelta(days=15) < value:
        return False

    if now - timedelta(days=15) > value:
        return False

    return True
