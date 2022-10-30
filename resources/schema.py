from flask import jsonify


def schema(obj: object) -> jsonify:
    """ Supports Song and Band object and returns a json. """
    id = obj.id
    name = obj.name
    album = obj.album

    return jsonify(id=id, name=name, album=album)


def genre_schema(obj: object) -> jsonify:
    """ Supports genre object and returns a json. """
    id = obj.id
    genre = obj.genre

    return jsonify(id=id, genre=genre)


def album_schema(obj: object) -> jsonify:
    """ Returns a json representation of the album schema. """

    id = obj.id
    name = obj.name

    songs = [_song.name for _song in obj.songs]  # list comprehension
    bands = obj.bands if obj.bands else None
    genres = obj.genres if obj.genres else None

    return jsonify(id=id,
                   name=name,
                   song_id=songs,
                   band_id=bands,
                   genre_id=genres)
