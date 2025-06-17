from server.config import db
from sqlalchemy_serializer import SerializerMixin

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurant_pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza')

    def __repr__(self):
        return f'<Pizza {self.id}: {self.name}, Ingredients: {self.ingredients}>'
