from flask import make_response, Blueprint, jsonify
from ..models.restaurant import Restaurant
from server.config import db

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_all_restaurants():
    restaurants = Restaurant.query.all()

    if restaurants:
        response = jsonify([restaurant.to_dict() for restaurant in restaurants])
        return response
    else:
        response = make_response({"Message": "No restaurants found"}, 404)
        return response
    
@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.filter_by(id=id).first()
    if restaurant:
        response = make_response(restaurant.to_dict(), 200)
        return response
    else:
        response = make_response({"error": "Restaurant not found"}, 404)
        return response
    
@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.filter_by(id=id).first()
    if restaurant:
        # Delete related restaurant_pizzas first to avoid foreign key constraint error
        from ..models.restaurant_pizza import RestaurantPizza
        related_rp = RestaurantPizza.query.filter_by(restaurant_id=id).all()
        for rp in related_rp:
            db.session.delete(rp)
        db.session.delete(restaurant)
        db.session.commit()
        return {"Message": "Restaurant deleted successfully"}, 200
    else:
        return {"error": "Restaurant not found"}, 404
