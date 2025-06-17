from flask import make_response, Blueprint, jsonify
from ..models.pizza import Pizza

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_all_pizzas():
    try:
        pizzas = Pizza.query.all()

        if pizzas:
            response = jsonify([pizz.to_dict() for pizz in pizzas])
            return response
        else:
            response = make_response({"Message": "No pizzas found"}, 404)
            return response
    except Exception as e:
        response = make_response({"error": str(e)}, 500)
        return response
