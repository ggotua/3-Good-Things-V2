from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .db import db
from . import login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    reflections = db.relationship('DailyReflection', backref='author', lazy=True)

    def __init__(self, username, email, password=None):
        self.username = username
        self.email = email
        if password:
            self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(int(user_id))

    @classmethod
    def create(cls, username, email, password):
        user = cls(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

class DailyReflection(db.Model):
    __tablename__ = 'daily_reflections'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    achievement_1 = db.Column(db.Text, nullable=False)
    achievement_2 = db.Column(db.Text, nullable=False)
    achievement_3 = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'date', name='unique_user_date_reflection'),
    )

    @classmethod
    def create(cls, user_id, date_str, achievement_1, achievement_2, achievement_3):
        # Parse date string if needed, depending on how it's passed
        if isinstance(date_str, str):
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        else:
            date_obj = date_str
            
        reflection = cls(
            user_id=user_id,
            date=date_obj,
            achievement_1=achievement_1,
            achievement_2=achievement_2,
            achievement_3=achievement_3
        )
        db.session.add(reflection)
        db.session.commit()
        return reflection

    @classmethod
    def get_by_user_and_date(cls, user_id, date_str):
        if isinstance(date_str, str):
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        else:
            date_obj = date_str
        return cls.query.filter_by(user_id=user_id, date=date_obj).first()

    @classmethod
    def get_user_reflections(cls, user_id, limit=7):
        return cls.query.filter_by(user_id=user_id).order_by(cls.date.desc()).limit(limit).all()

    def update(self, achievement_1=None, achievement_2=None, achievement_3=None):
        if achievement_1 is not None:
            self.achievement_1 = achievement_1
        if achievement_2 is not None:
            self.achievement_2 = achievement_2
        if achievement_3 is not None:
            self.achievement_3 = achievement_3
        
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
