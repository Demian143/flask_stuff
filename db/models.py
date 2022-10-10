from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Record(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    band: str = db.Column(db.String('100'), unique=True)
    album: str = db.Column(db.String('100'), unique=True)
    genre: str = db.Column(db.String('100'))
