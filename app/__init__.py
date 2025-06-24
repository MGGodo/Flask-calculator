from flask import Flask
from pymongo import MongoClient
import os

def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    # Conection with MongoDB
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://mongadmin:adminmongo.@localhost:27017/')
    client = MongoClient(MONGO_URI)

    # DB mongo-calc
    app.config["MONGO"] = client["mongo-server"]

    # Import and register the calculator blueprint 
    from .routes.calculator import calculator_bp
    app.register_blueprint(calculator_bp)

    # Return the app instance
    return app
