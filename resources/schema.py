from flask import jsonify


def schema(record: object) -> jsonify:
    band = record.band
    album = record.album
    genre = record.genre if record.genre else None

    return jsonify(band=band, album=album, genre=genre)
