from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, send_from_directory, current_app
from flask_login import login_required, current_user
from datetime import datetime
from .models import DailyReflection
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Serve the Svelte app
    return send_from_directory(os.path.join(current_app.root_path, 'static/dist'), 'index.html')

@main.route('/<path:path>')
def static_proxy(path):
    # Serve static files from dist
    if os.path.exists(os.path.join(current_app.root_path, 'static/dist', path)):
        return send_from_directory(os.path.join(current_app.root_path, 'static/dist'), path)
    # Otherwise serve index.html for client-side routing
    return send_from_directory(os.path.join(current_app.root_path, 'static/dist'), 'index.html')

@main.route('/api/dashboard')
@login_required
def dashboard():
    today = datetime.now().date()
    today_reflection_obj = DailyReflection.get_by_user_and_date(current_user.id, today.strftime('%Y-%m-%d'))
    recent_reflections_objs = DailyReflection.get_user_reflections(current_user.id)
    
    today_reflection = None
    if today_reflection_obj:
        today_reflection = {
            'id': today_reflection_obj.id,
            'achievement_1': today_reflection_obj.achievement_1,
            'achievement_2': today_reflection_obj.achievement_2,
            'achievement_3': today_reflection_obj.achievement_3
        }
        
    recent_reflections = [{
        'id': r.id,
        'date': r.date,
        'achievement_1': r.achievement_1,
        'achievement_2': r.achievement_2,
        'achievement_3': r.achievement_3
    } for r in recent_reflections_objs]

    return jsonify({
        'user': {'username': current_user.username},
        'today_reflection': today_reflection,
        'recent_reflections': recent_reflections,
        'today': today.strftime('%Y-%m-%d')
    })

@main.route('/api/reflect', methods=['POST'])
@login_required
def reflect():
    today = datetime.now().date()
    data = request.get_json()
    
    achievement_1 = data.get('achievement_1')
    achievement_2 = data.get('achievement_2')
    achievement_3 = data.get('achievement_3')
    
    if not all([achievement_1, achievement_2, achievement_3]):
        return jsonify({'error': 'Missing achievements'}), 400
    
    existing_reflection = DailyReflection.get_by_user_and_date(
        current_user.id, 
        today.strftime('%Y-%m-%d')
    )
    
    if existing_reflection:
        existing_reflection.update(
            achievement_1=achievement_1,
            achievement_2=achievement_2,
            achievement_3=achievement_3
        )
    else:
        DailyReflection.create(
            current_user.id,
            today.strftime('%Y-%m-%d'),
            achievement_1,
            achievement_2,
            achievement_3
        )
    
    return jsonify({'success': True})
