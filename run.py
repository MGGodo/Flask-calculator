from app import create_app

app = create_app()  # Create the Flask app instance

if __name__ == '__main__':
    # Run the app (debug mode)
    app.run(debug=True)
