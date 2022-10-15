from flask_restful import Resource
from db.models import db, Album, Song, Band, Genre
from flask import request
from resources.schema import schema, album_schema, genre_schema


class QueryAlbums(Resource):
    def get(self):
        # example: GET /albums/?name='deftones'
        name = request.args.get('name')
        if name:
            album = db.get_or_404(Album, name)
            return album_schema(album)

    def post(self):
        # example: POST /albums/?name='homs'&song_id=1&band_id=1&genre_id=2
        name = request.args.get('name')
        song_id = request.args.get('song_id')
        band_id = request.args.get('band_id')
        genre_id = request.args.get('genre_id')

        if name:
            # You need at least the name to register a new album
            new_album = Album(name=name,
                              song_id=song_id,
                              band_id=band_id,
                              genre_id=genre_id)

            db.session.add(new_album)
            db.session.commit()
        else:
            return "At least one name is needed to register a new album"


class QuerySongs(Resource):
    def get(self):
        # example: GET /songs/?name='shove it'
        name = request.args.get('name')
        if name:
            song = db.get_or_404(Song, name)
            return schema(song)

    def post(self):
        # example: POST /songs/?name='shove it'
        name = request.args.get('name')
        if name:
            new_song = Song(name=name)
            db.session.add(new_song)
            db.session.commit()

            return schema(new_song)


class QueryBands(Resource):
    def get(self):
        # example: GET /bands/?name='shove it'
        name = request.args.get('name')
        if name:
            band = db.get_or_404(Band, name)
            return schema(band)

    def post(self):
        # example: POST /bands/?name='deftones'
        name = request.args.get('name')
        if name:
            new_band = Band(name=name)
            db.session.add(new_band)
            db.session.commit()

            return schema(new_band)


class QueryGenres(Resource):
    def get(self):
        # example: GET /genres/?name='Nu Metal'
        name = request.args.get('name')
        if name:
            genre = db.get_or_404(Genre, name)
            return genre_schema(genre)

    def post(self):
        # example: POST /genres/?name='Nu Metal'
        name = request.args.get('name')
        if name:
            new_genre = Genre(genre=name)
            db.session.add(new_genre)
            db.session.commit()
            return genre_schema(new_genre)
