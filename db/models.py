from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    # ForeignKeys
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
    band_id = db.Column(db.Integer, db.ForeignKey('band.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    # relationship
    relation = db.relationship('Album', backref='song', lazy=True)


class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    # relationship
    relation = db.relationship('Album', backref='band', lazy=True)


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), unique=True)

    # relationship
    relation = db.relationship('Album', backref='genre', lazy=True)
