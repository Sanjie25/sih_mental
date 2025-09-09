from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from api import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    # points = db.Column(db.Integer, nullable=False)
    # appointments_id = db.Column(db.Integer)

    # Delete orphan appointments if they exist
    # appointments = db.relationship(
    #    "Appointment", backref="user", cascade="all, delete-orphan"
    # )
    # conditions = db.relationship("Condition", backref="user")
    # Delete orphan goals if they exist
    # goals = db.relationship("Goal", backref="user", cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(
            password, method="pbkdf2:sha256", salt_length=4
        )

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User %r>" % self.username
