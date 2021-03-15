from flask import Flask, request, jsonify, session
from flask_socketio import SocketIO, emit
from flask_cors import CORS

from io import StringIO

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)

from werkzeug.exceptions import InternalServerError

from .convert import MongoJSONEncoder, ObjectIdConverter
from . import db

import traceback

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_mapping(
        SECRET_KEY='6h6QiNgtCRqZazw3lpdSW87k2J604ElubccVH6fB6vWrvaECGLy14cnFg8brGjD',
        JWT_SECRET_KEY="q6wLVfDr5tFbNnQf1ORgME2bOXyioYL63DYWcEMgfqIswuKPstUFfClD8807EJv",
        JWT_ACCESS_TOKEN_EXPIRES=False,
        DATABASE='planner_mongodb:27017/planner',
    )
    jwt = JWTManager(app)

    db.init_app(app)
    with app.app_context():
        db.init_db()

    app.json_encoder = MongoJSONEncoder
    app.url_map.converters['objectid'] = ObjectIdConverter

    from .api import bp
    app.register_blueprint(bp)

    # @app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    #     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    #     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    #     response.headers.add('Access-Control-Allow-Credentials', 'true')
    #     return response

    return app


# if __name__ == '__main__':
#     print('here')
#     app = create_app()
#     socket.socketio.run(app, debug=True)
