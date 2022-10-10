from flask_restful import Resource
from db.models import Record
from flask import request


class QueryAlbum(Resource):
    def get(self):
        id = request.args.get('id')
        band = request.args.get('band')
        album = request.args.get('album')

        if id:
            return Record.query.get(id)
        if band:
            return Record.query.get(band)
        if album:
            return Record.query.get(album)

        return Record.query.all()
