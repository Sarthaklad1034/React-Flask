# # backend/server.py
# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from database import UserDatabase
# import os

# # Initialize Flask app
# app = Flask(__name__, 
#             static_folder='../frontend/build', 
#             static_url_path='/')
# CORS(app)

# # Initialize database
# user_db = UserDatabase()

# @app.route('/')
# def serve():
#     return send_from_directory(app.static_folder, 'index.html')

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     username = data.get('username')
#     password = data.get('password')
    
#     # Validate user
#     role = user_db.validate_user(username, password)
    
#     if role:
#         return jsonify({
#             'success': True, 
#             'role': role, 
#             'message': 'Login successful'
#         }), 200
#     else:
#         return jsonify({
#             'success': False, 
#             'message': 'Invalid credentials'
#         }), 401

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database import UserDatabase
import os

# Initialize Flask app
app = Flask(__name__, 
            static_folder='../build', 
            static_url_path='/')
CORS(app)

# Initialize database
user_db = UserDatabase()

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Validate user
    role = user_db.validate_user(username, password)
    
    if role:
        return jsonify({
            'success': True, 
            'role': role, 
            'message': 'Login successful'
        }), 200
    else:
        return jsonify({
            'success': False, 
            'message': 'Invalid credentials'
        }), 401

if __name__ == "__main__":
    app.run(debug=True)