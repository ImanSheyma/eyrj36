import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB

DB_URI = os.getenv("DB_URI")

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB, nullable=False)


def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    db.init_app(app)
    
    with app.app_context():
        db.create_all()