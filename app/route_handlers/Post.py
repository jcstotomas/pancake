from ..database.models import Post
from app.route_handlers import bp
from app import db
from flask import request, jsonify



# define the create post route 

@bp.route('posts', methods=["POST", "GET"])
def create_post():
    body = request.get_json()
    new_post = Post(user_id=5)
    db.session.add(new_post)
    db.session.commit()
    return "post created"


@bp.route('posts/<id>', methods=['GET'])
def delete_post(id):
    post = db.session.query(Post).filter_by(post_id=id).first()
    db.session.delete(post)
    db.session.commit()
    return "post deleted"

@bp.route('posts', methods=['UPDATE'])
def update_post():
    pass


@bp.route('posts', methods=['GET'])
def get_post():
    pass