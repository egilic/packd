from flask import Blueprint, request, jsonify
from .. import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=['POST'])
def signup():
    from ..models import User

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400
    
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "User with that username or email already exists"}), 400
    
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201

@bp.route('/login', methods=['POST'])
def login():
    from ..models import User
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401

    # For now, just return a success message 
    # TODO: later replace with session
    return jsonify({"message": "Login successful"}), 200