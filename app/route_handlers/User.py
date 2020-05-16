from ..database.models import User
from app.route_handlers import bp
from app import db
from .response_template import success_response, error_response
from flask import request

@bp.route("users", methods=["POST"])
def create_user():
    body  = request.get_json()
    for field in body:
        print(field)
    new_user = User(name=body["name"], email=body["email"], username=body["username"])
    db.session.add(new_user)
    db.session.commit()
    return success_response(200, message="User created successfully")


@bp.route("users/<username>", methods=["GET"])
def get_user(username):
    user = db.session.query(User).filter_by(username=username).first()
    return success_response(200, payload=user, message="user data received")


@bp.route("users/<username>/delete", methods=["GET"])
def delete_user(username):
    user = db.session.query(User).filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()
    return success_response(200, message="Deleted user successfully")


@bp.route("users/<username>", methods=["PUT"])
def update_user(username):
    user = db.session.query(User).filter_by(username=username).first()
    db.session.update(user)
    return success_response(200, message="Updated user successfully")



