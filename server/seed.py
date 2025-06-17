from server.app import app
from server.config import db

# Import models only after app context is available to avoid circular imports
with app.app_context():
    from server.models.pizza import Pizza
    from server.models.restaurant import Restaurant
    from server.models.restaurant_pizza import RestaurantPizza

    # Clear existing data
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    # Create seed data
    r1 = Restaurant(name="Big Square", address="13 Main Street")
    r2 = Restaurant(name="Pizza Inn", address="14 Side Street")

    p1 = Pizza(name="Pepperoni", ingredients="cheese, pepperoni, tomato sauce")
    p2 = Pizza(name="Veggie", ingredients="bell peppers, olives, mushrooms, onions")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=15, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=10, restaurant_id=r2.id, pizza_id=p2.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()