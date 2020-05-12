from ..database.models import User
from app.route_handlers import bp
from app import db
from .response_template import success_response, error_response

@bp.route("users", methods=["GET", "POST"])
def create_user():
    new_user = User(name="ASdf", email="asdff@yahoo.com", username="jeremy")
    db.session.add(new_user)
    db.session.commit()
    return success_response(200, message="User created successfully")


@bp.route("users/<username>", methods=["GET"])
def get_user(username):
    user = db.session.query(User).filter_by(username=username).first()
    print(user)
    return str(user)



