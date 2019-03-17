from server import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Schedule(db.Model):
    pasp_id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)
    pare1 = db.Column(db.String(20), nullable=True)
    pare2 = db.Column(db.String(20), nullable=True)
    pare3 = db.Column(db.String(20), nullable=True)
    pare4 = db.Column(db.String(20), nullable=True)
    pare5 = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"Schedule('{self.day}', '{self.pare1}', '{self.pare2}', '{self.pare3}', '{self.pare4}', '{self.pare5}')"
