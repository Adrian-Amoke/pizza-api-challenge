from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from dotenv import load_dotenv
import os
from server.controllers.pizza_controller import pizza_bp
from server.controllers.index_controller import index_bp
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.restaurant_pizza_controller import restaurantpizza_bp
from server.config import db

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})

migrate = Migrate()


app = Flask(__name__)

load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

import server.models

app.register_blueprint(pizza_bp)
app.register_blueprint(index_bp)
app.register_blueprint(restaurant_bp)
app.register_blueprint(restaurantpizza_bp)

db.init_app(app)
migrate.init_app(app, db)

if __name__ == "__main__":
    app.run(debug=True, port=5555)