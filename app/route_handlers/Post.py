from ..database.models import Post
from app.route_handlers import bp
from app import db
from flask import request, jsonify



# define the create post route 

@bp.route('posts', methods=["POST"])
def create_post():
    body = request.get_json()
    new_post = Post()
    db.session.add(new_post)
    db.session.commit()
    return "post created"


@bp.route('posts', methods=['DELETE'])
def delete_post():
    pass

@bp.route('posts', methods=['UPDATE'])
def update_post():
    pass


@bp.route('posts', methods=['GET'])
def get_post():
    pass