from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv() # Load the env variables

    # Create the Flask application instance
    app = Flask(__name__)

    # Conection with MongoDB
    MONGO_URI = os.environ.get("MONGO_URI")
    client = MongoClient(MONGO_URI)

    # DB mongo-calc
    app.config["MONGO"] = client["mongo-calc"]

    # Import and register the calculator blueprint 
    from .routes.calculator import calculator_bp
    app.register_blueprint(calculator_bp)

    # Return the app instance
    return app
