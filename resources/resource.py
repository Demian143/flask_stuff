from flask_restful import Resource
from db.models import Record


class QueryAlbum(Resource):
    def get(self):
        return Record.query.all()
