from flask import Blueprint, request, jsonify
from models import Faculty
from werkzeug.security import check_password_hash
from models import db

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    faculty = Faculty.query.filter_by(email=data['email']).first()
    if faculty and check_password_hash(faculty.password, data['password']):
        return jsonify({"message": "Login successful", "faculty_id": faculty.id}), 200
    return jsonify({"message": "Invalid credentials"}), 401
