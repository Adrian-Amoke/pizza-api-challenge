from flask import make_response, Blueprint
from server.models import Restaurant
from server.config import db

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_all_restaurants():
    restaurants = Restaurant.query.all()

    if restaurants:
        response = make_response(restaurant.to_dict() for restaurant in restaurants)
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
        db.session.delete(restaurant)
        db.session.commit()