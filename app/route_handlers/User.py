from ..database.models import User
from app.route_handlers import bp
from app import db

@bp.route("user", methods=["GET", "POST"])
def create_user():
    new_user = User(name="ASdf")
    db.session.add(new_user)
    db.session.commit()
    return "created"


