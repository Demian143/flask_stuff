from flask import jsonify


def schema(obj: object) -> jsonify:
    """ Supports Song and Band object and returns a json. """
    id = obj.id
    name = obj.name

    return jsonify(id=id, name=name)


def genre_schema(obj: object) -> jsonify:
    """ Supports genre object and returns a json. """
    id = obj.id
    genre = obj.genre

    return jsonify(id=id, genre=genre)


def album_schema(obj: object) -> jsonify:
    """ Returns a json representation of the album schema. """

    id = obj.id
    name = obj.name

    song_id = obj.song_id if obj.song_id else None
    band_id = obj.band_id if obj.band_id else None
    genre_id = obj.genre_id if obj.genre_id else None

    return jsonify(id=id,
                   name=name,
                   song_id=song_id,
                   band_id=band_id,
                   genre_id=genre_id)
