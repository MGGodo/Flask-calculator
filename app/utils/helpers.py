from flask import request, current_app

# Extracts two numbers (a and b) from the JSON body of the request.
# Expects the JSON to have the format: {"a": x, "b": y}
def get_numbers():
    data = request.get_json()
    return data["a"], data["b"]


# Save deta in specific collection
def save_in_col(operation, a, b, result):
    mongo = current_app.config["MONGO"]
    collection = mongo[operation]  # Use the name of the operation as the name of the collection
    collection.insert_one({
        "a": a,
        "b": b,
        "result": result
    })