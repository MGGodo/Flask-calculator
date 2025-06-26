from flask import Flask, request, jsonify, Blueprint, current_app
from app.utils.helpers import get_numbers, save_in_col  # Import the helper's function

# Create a blueprint named 'calculator'
calculator_bp = Blueprint('calculator', __name__)

# Add two numbers
@calculator_bp.route('/addition', methods=['POST'])
def addition():
    a, b,  = get_numbers()
    result = a + b
    save_in_col("addition", a, b, result)
    return jsonify({"a": a, "b": b, "res-add": result})

# Subtract two numbers
@calculator_bp.route('/subtraction', methods=['POST'])
def subtraction():
    a, b,  = get_numbers()
    result = a - b
    save_in_col("subtraction", a, b, result)
    return jsonify({"a": a, "b": b, "res-sub": result})

# Multiply two numbers
@calculator_bp.route('/multiplication', methods=['POST'])
def multiplication():
    a, b,  = get_numbers()
    result = a * b
    save_in_col("multiplication", a, b, result)
    return jsonify({"a": a, "b": b, "res-mult": result})

# Divide two numbers
@calculator_bp.route('/division', methods=['POST'])
def division():
    a, b,  = get_numbers()
    result = None if b == 0 else a / b
    save_in_col("division", a, b, result)
    return jsonify({"a": a, "b": b, "res-div": result})

# Returns the result of the 4 operations +, -, *, /
@calculator_bp.route('/all-op', methods=['POST'])
def all():
    a, b,  = get_numbers()
    results = {
        "a": a,
        "b": b,
        "res-add": a + b,
        "res-sub": a - b,
        "res-mult": a * b,
        "res-div": None if b == 0 else a / b
    }

    mongo = current_app.config["MONGO"]
    mongo["all-op"].insert_one(results.copy())

    return jsonify(results)

