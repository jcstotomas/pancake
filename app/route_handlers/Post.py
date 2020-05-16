from ..database.models import Post
from app.route_handlers import bp
from app import db
from flask import request, jsonify



# define the create post route 

@bp.route('posts', methods=["POST"])
def create_post():
    body = request.get_json()
    new_post = Post(user_id=5)
    db.session.add(new_post)
    db.session.commit()
    return "post created"


@bp.route('posts/<id>', methods=['DELETE'])
def delete_post(id):
    post = db.session.query(Post).filter_by(post_id=id).first()
    db.session.delete(post)
    db.session.commit()
    return "post deleted"

@bp.route('posts/<id>', methods=['PUT'])
def update_post(id):
    body = request.get_json()
    
    post = db.session.query(Post).filter_by(post_id=id).first()
    # for updated_field in body:
    #     setattr(post, updated_field, User.updated_field = body[updated_field])
    post.text_content = body["text_content"]
    db.session.commit()
    return "post updated"


@bp.route('posts/<id>', methods=['GET'])
def get_post(id):
    post = db.session.query(Post).filter_by(post_id=id).first()
    return jsonify(post.return_info())
