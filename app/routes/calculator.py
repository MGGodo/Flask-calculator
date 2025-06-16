from flask import Flask, request, jsonify, Blueprint
from app.utils.helpers import get_numbers  # Import the helper function

# Create a blueprint named 'calculator'
calculator_bp = Blueprint('calculator', __name__)

def get_numbers():
    data = request.get_json()
    return data["a"], data["b"]

# Add two numbers
@calculator_bp.route('/addition', methods=['POST'])
def addition():
    a, b,  = get_numbers()
    return jsonify({"a": a, "b": b, "res-add": a + b})

# Subtract two numbers
@calculator_bp.route('/subtraction', methods=['POST'])
def subtraction():
    a, b,  = get_numbers()
    return jsonify({"a": a, "b": b, "res-sub": a - b})

# Multiply two numbers
@calculator_bp.route('/multiplication', methods=['POST'])
def multiplication():
    a, b,  = get_numbers()
    return jsonify({"a": a, "b": b, "res-mult": a * b})

# Divide two numbers
@calculator_bp.route('/division', methods=['POST'])
def division():
    a, b,  = get_numbers()
    return jsonify({"a": a, "b": b, "res-div": None if b == 0 else a / b})

# Returns the result of the 4 operations +, -, *, /
@calculator_bp.route('/all-op', methods=['POST'])
def all():
    a, b,  = get_numbers()
    return jsonify({
        "a": a,
        "b": b,
        "res-add": a + b,
        "res-sub": a - b,
        "res-mult": a * b,
        "res-div": None if b == 0 else a / b
    })

