from flask import Blueprint, jsonify

bp = Blueprint('route_handlers',__name__)

@bp.route('/', methods=['GET'])
def api_status():
    return jsonify({"status": "success"})

import app.route_handlers.User