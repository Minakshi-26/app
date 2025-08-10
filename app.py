from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

@app.route('/')
def home():
    return "Welcome to the User API!"

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get single user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user})
    return jsonify({"error": "User not found"}), 404

# Create user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get("id")
    name = data.get("name")
    if not user_id or not name:
        return jsonify({"error": "ID and name required"}), 400
    if user_id in users:
        return jsonify({"error": "User ID already exists"}), 400
    users[user_id] = {"name": name}
    return jsonify({"message": "User created"}), 201

# Update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    users[user_id]["name"] = name
    return jsonify({"message": "User updated"})

# Delete user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

