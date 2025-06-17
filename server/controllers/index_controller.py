from flask import Blueprint,make_response

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    response = make_response({"Message": "Welcome to Pizza Restaurant"}, 200)
    return response