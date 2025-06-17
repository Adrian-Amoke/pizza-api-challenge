from flask import Flask
from flask_migrate import Migrate
from server.config import db
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)
app.config.from_prefixed_env()

db.init_app(app=app)

migrate=Migrate(app=app,db=db)

from server.controllers.index_controller import index_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.restaurant_pizza_controller import restaurantpizza_bp

app.register_blueprint(index_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_bp)
app.register_blueprint(restaurantpizza_bp)


if __name__ == '__main__':
    app.run(port=5555, debug=True)