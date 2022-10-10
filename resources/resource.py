from flask_restful import Resource


class QueryAlbum(Resource):
    def get(self):
        return {"test": "test"}, 200
