from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band = db.Column(db.String(100), unique=True)
    album = db.Column(db.String(100), unique=True)
    genre = db.Column(db.String(100))
