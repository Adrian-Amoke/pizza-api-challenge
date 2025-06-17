from flask import make_response, Blueprint, request
from ..models.restaurant_pizza import RestaurantPizza
from server.config import db

restaurantpizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurantpizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not price or not pizza_id or not restaurant_id:
        response = make_response({"errors": ["missing required keys"]}, 400)
        return response
    
    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(restaurant_pizza)
    db.session.commit()
    response = make_response(restaurant_pizza.to_dict(), 201)
    return response

