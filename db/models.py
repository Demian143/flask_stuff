from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    # relationship
    band = db.relationship('Band', backref='album', lazy=True)
    song = db.relationship('Song', backref='album', lazy=True)
    genre = db.relationship('Genre', backref='album', lazy=True)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    # relationship
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))


class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    # relationship
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), unique=True)

    # relationship
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
