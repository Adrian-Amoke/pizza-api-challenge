from server.config import db
from sqlalchemy_serializer import SerializerMixin

class Restaurant(db.Model, SerializerMixin):
    serialize_rules = ('-restaurant_pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant')

    def __repr__(self):
        return f'<Restaurant {self.id}: {self.name}, Address: {self.address}>'
