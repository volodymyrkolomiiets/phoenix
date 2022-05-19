# application/user_api/routes.py
from . import user_api_blueprint
from .. import db, login_manager
from ..models import User
from flask import make_response, jsonify
from flask_login import current_user, login_user, logout_user, login_required

from passlib.hash import sha256_crypt


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get("Authorization")
    if api_key:
        api_key = api_key.replace("Basic ", "", 1)
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user
    return None


@user_api_blueprint.route("/api/users", methods=["GET"])
def gets_users():
    data = []
    for row in User.query.all():
        data.append(row.to_json())

    response = jsonify(data)
    return response




