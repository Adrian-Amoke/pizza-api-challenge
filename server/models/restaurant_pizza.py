from server.app import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f'<RestaurantPizza {self.id}: Pizza ID: {self.pizza_id}, Restaurant ID: {self.restaurant_id}, Price: {self.price}>'
    
    @validates('price')
    def validate_price(self, key, value):
        if value < 1 or value > 30:
            raise ValueError("Price must be between 1 and 30")
        return value