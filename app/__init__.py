from flask import Flask

def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    # Import and register the calculator blueprint 
    from .routes.calculator import calculator_bp
    app.register_blueprint(calculator_bp)

    # Return the app instance
    return app
