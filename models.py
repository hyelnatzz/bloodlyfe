from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class User(db.Model):
    """Model for user accounts."""
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                primary_key=True)
    username = db.Column(db.String,
                nullable=False,
                unique=False)
    first_name = db.Column(db.String,
                nullable=False,
                unique=False)
    last_name = db.Column(db.String,
                nullable=False,
                unique=False)
    email = db.Column(db.String(40),
                unique=True,
                nullable=False)
    password = db.Column(db.String(200),
                primary_key=False,
                unique=False,
                nullable=False)
    def __repr__(self):
        return '<User {}>'.format(self.username)

db.create_all()
