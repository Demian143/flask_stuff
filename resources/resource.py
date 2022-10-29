from flask_restful import Resource
from db.models import db, Album, Song, Band, Genre
from flask import request
from resources.schema import schema, album_schema, genre_schema


class QueryAlbums(Resource):
    def get(self):
        # example: GET /albums/?name='deftones' or /albums/?id=3
        name = request.args.get('name')
        if name:
            album = db.one_or_404(db.select(Album).filter_by(name=name))
            return album_schema(album)

        id = request.args.get('id')
        if id:
            album = db.one_or_404(db.select(Album).filter_by(id=id))
            return album_schema(album)

        else:
            return {"message": "No album found, try adding ?name=<album> after the url."}

    def post(self):
        # example: POST /albums/?name='homs'&song_id=1&band_id=1&genre_id=2
        name = request.args.get('name')
        # song_id = request.args.get('song_id')
        # band_id = request.args.get('band_id')
        # genre_id = request.args.get('genre_id')

        # breakpoint()
        if name:
            new_album = Album(name=name)

            db.session.add(new_album)
            db.session.commit()

            album = db.one_or_404(db.select(Album).filter_by(name=name))
            return album_schema(album)
        else:
            return {"message": "At least one name is required."}

    def delete(self):
        # example: DELETE /albums/?name='deftones'
        name = request.args.get('name')
        if name:
            album = db.one_or_404(db.select(Album).filter_by(name=name))
            db.session.delete(album)
            db.session.commit()

            return album_schema(album)

        else:
            return {"message": "No album found, try adding ?name=<album> after the url."}

    def patch(self):
        # example: POST /albums/?id=<1>&<key>=<value>
        name = request.args.get('name')
        song_id = request.args.get('song_id')
        band_id = request.args.get('band_id')
        genre_id = request.args.get('genre_id')

        # breakpoint()
        id = request.args.get('id')
        if id:
            album = db.one_or_404(db.select(Album).filter_by(id=id))
            if name:
                album.name = name
            if song_id:
                album.songs.append(db.one_or_404(
                    db.select(Song).filter_by(id=song_id)))
            if band_id:
                album.bands = band_id
            if genre_id:
                album.genres.append(db.one_or_404(
                    db.select(Genre).filter_by(id=genre_id)))

            db.session.commit()
            return album_schema(album)


class QuerySongs(Resource):
    def get(self):
        # example: GET /songs/?name='shove it'
        name = request.args.get('name')
        if name:
            song = db.one_or_404(db.select(Song).filter_by(name=name))
            return schema(song)

        id = request.args.get('id')
        if id:
            song = db.one_or_404(db.select(Song).filter_by(id=id))
            return schema(song)

        else:
            return {"message": "No song found, try adding ?name=<song> after the url."}

    def post(self):
        # example: POST /songs/?name='shove it'
        name = request.args.get('name')
        if name:
            new_song = Song(name=name)
            db.session.add(new_song)
            db.session.commit()

            return schema(new_song)

    def delete(self):
        # example: DELETE /songs/?name='shove it'
        name = request.args.get('name')
        if name:
            song = db.one_or_404(db.select(Song).filter_by(name=name))
            db.session.delete(song)
            db.session.commit()

            return schema(song)

        else:
            return {"message": "No album found, try adding ?name=<song> after the url."}


class QueryBands(Resource):
    def get(self):
        # example: GET /bands/?name='shove it'
        name = request.args.get('name')
        if name:
            band = db.get_or_404(Band, name)
            return schema(band)
        else:
            return {"message": "No band found, try adding ?name=<band> after the url."}

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
        breakpoint()
        name = request.args.get('name')
        if name:
            genre = db.get_or_404(Genre, name)
            return genre_schema(genre)
        else:
            return {"message": "No genre found, try adding ?genre=<genre> after the url."}

    def post(self):
        # example: POST /genres/?name='Nu Metal'
        name = request.args.get('name')
        if name:
            new_genre = Genre(genre=name)
            db.session.add(new_genre)
            db.session.commit()
            return genre_schema(new_genre)
