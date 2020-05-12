from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def success_response(response_code, payload=None, message=None):
    response_object = {"status": HTTP_STATUS_CODES.get(response_code, "OK")}
    response_object["data"] = payload
    response_object["message"] = message
    response_object = jsonify(response_object)
    return response_object


def error_response(response_code, message=None):
    response_object = {"status": HTTP_STATUS_CODES.get(response_code, "ERROR")}
    response_object["message"] = message
    response_object = jsonify(response_object)
    return response_object

    
