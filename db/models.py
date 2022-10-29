from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    # relationships
    # I'm gonna keep only one band
    bands = db.relationship('Band', backref='album_ref', lazy=True)
    songs = db.relationship('Song', backref='album_ref', lazy=True)
    genres = db.relationship('Genre', backref='album_ref', lazy=True)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    # ForeignKey
    album = db.Column(db.Integer, db.ForeignKey('album.id'))


class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    # ForeignKey
    album = db.Column(db.Integer, db.ForeignKey('album.id'))


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), unique=True)

    # ForeignKey
    album = db.Column(db.Integer, db.ForeignKey('album.id'))
