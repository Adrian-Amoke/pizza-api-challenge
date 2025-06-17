from flask import make_response, Blueprint
from ..models.pizza import Pizza

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_all_pizzas():
    pizzas = Pizza.query.all()

    if pizzas:
        response = make_response(pizz.to_dict() for pizz in pizzas)
        return response
    else:
        response = make_response({"Message": "No pizzas found"}, 404)
        return response
