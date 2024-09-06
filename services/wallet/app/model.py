# /wallet/app/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, default=0.0)
