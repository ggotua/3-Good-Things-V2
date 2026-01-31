from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    # Check if user already exists
    existing_user = User.get_by_username(username)
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400
    
    # Create new user
    new_user = User.create(username, email, password)
    
    return jsonify({'success': True, 'message': 'Registration successful'})

@auth.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.get_by_username(username)
    
    if user and user.check_password(password):
        login_user(user)
        return jsonify({'success': True, 'user': {'username': user.username, 'email': user.email}})
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@auth.route('/api/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'success': True})

@auth.route('/api/user')
def get_user():
    if current_user.is_authenticated:
        return jsonify({'authenticated': True, 'user': {'username': current_user.username, 'email': current_user.email}})
    return jsonify({'authenticated': False}), 401
