from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Record(db.Model):
    band = db.Column(db.String(100), unique=True, primary_key=True)
    album = db.Column(db.String(100), unique=True)
    genre = db.Column(db.String(100))
