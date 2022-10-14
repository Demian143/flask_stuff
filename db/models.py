from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100))

    # relationship
    band = db.relationship('Band', backref='')


class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String(100))

    # relationship


class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band = db.Column(db.String(100), unique=True)

    # relationship
