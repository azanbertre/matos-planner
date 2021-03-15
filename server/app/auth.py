from app.db import get_db
from app.models.users.User import User

from flask import g
from bson import ObjectId


def current_user() -> User:
    """ Return current logged in user

        @return : User
    """

    if not g.user:
        return None

    return g.user

def user_exists(data: dict) -> bool:
    """ Check if user exists

        @param data : dict \n
        @return : bool
    """

    db = get_db()

    return bool(db.users.find_one({'$or': [
        {'username': data.get('username')},
        {'email': data.get('email')}
    ]}, {'_id': 1}))

def get_user(data: dict, projection: dict=None) -> dict:
    """ Return user by username or email

        @param data : dict \n
        @param projection : dict \n
        @return : User
    """

    db = get_db()

    if projection:
        return db.users.find_one({'$or': [
            {'username': data.get('username')},
            {'email': data.get('email')}
        ]}, projection)

    return db.users.find_one({'$or': [
        {'username': data.get('username')},
        {'email': data.get('email')}
    ]})

def get_user_by_id(user_id: ObjectId, projection: dict=None) -> dict:
    """ Return user by user id

        @param user_id : ObjectId \n
        @param projection : dict \n
        @return : User
    """

    db = get_db()

    if projection:
        return db.users.find_one({'_id': user_id}, projection)

    return db.users.find_one({'_id': user_id})

def get_user_permissions(user:dict={}) -> list:
    """ Return user permissions

        @param user : User \n
        @return : list
    """

    db = get_db()

    if not user:
        user = current_user()

    user_groups = get_user_groups(user)

    permission_ids = [
        p_id for ug in user_groups for p_id in ug['permissions']
    ] # + user.get('customPermissions', [])

    return list(db.permissions.find({'_id': {'$in': permission_ids}}))

def get_user_groups(user: dict={}) -> list:
    """ Return user groups

        @param user : User \n
        @return : list
    """

    db = get_db()

    if not user:
        user = current_user()

    return list(db.groups.find({
        'slug': {'$in': user['groups']}
    }))

def has_permission(user: dict={}, slug: str=None) -> bool:
    """ Check if user has permission

        @param user : User \n
        @param slug : str \n
        @return : bool
    """

    db = get_db()

    permission = db.permissions.find_one({'slug': slug})
    user_permissions = get_user_permissions(user)

    return bool(permission and any([
        permission['_id'] == up['_id'] for up in user_permissions
    ]))

def has_group(user: dict={}, slug: str=None) -> bool:
    """ Check if user has group

        @param user : User \n
        @param slug : str \n
        @return : bool
    """

    db = get_db()

    group = db.groups.find_one({'slug': slug})
    user_groups = get_user_groups(user)

    return bool(group and any([
        group['_id'] == ug['_id'] for ug in user_groups
    ]))
