from flask import Flask, request, jsonify

app = Flask(__name__)

def get_numbers():
    data = request.get_json()
    return data["a"], data["b"]

# Add two numbers
@app.route('/addition', methods=['POST'])
def addition():
    a, b,  = get_numbers()
    return jsonify({"a": a, "b": b, "res-add": a + b})

# Subtract two numbers
@app.route('/subtraction', methods=['POST'])
def subtraction():
    a, b,  = get_numbers()
    return jsonify({"a": a, "b": b, "res-sub": a - b})

# Multiply two numbers
@app.route('/multiplication', methods=['POST'])
def multiplication():
    a, b,  = get_numbers()
    return jsonify({"a": a, "b": b, "res-mult": a * b})

# Divide two numbers
@app.route('/division', methods=['POST'])
def division():
    a, b,  = get_numbers()
    return jsonify({"a": a, "b": b, "res-div": None if b == 0 else a / b})

# Returns the result of the 4 operations +, -, *, /
@app.route('/all-op', methods=['POST'])
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
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
