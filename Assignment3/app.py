
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# Dummy user data (replace with database integration)
users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'}
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users and users[username]['password'] == password:
        # Generate JWT token here if needed
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if _name_ == '_main_':
    app.run(debug=True)