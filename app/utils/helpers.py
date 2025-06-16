from flask import request

# Extracts two numbers (a and b) from the JSON body of the request.
# Expects the JSON to have the format: {"a": x, "b": y}
def get_numbers():
    data = request.get_json()
    return data["a"], data["b"]
