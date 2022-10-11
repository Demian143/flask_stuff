from flask_restful import Resource
from db.models import Record, db
from flask import request
from resources.schema import schema


class QueryAlbum(Resource):
    def get(self):
        band = request.args.get('band')
        album = request.args.get('album')
        genre = request.args.get('genre')

        if band:
            rec = db.get_or_404(Record, band)
            return schema(rec)
        if album:
            rec = db.first_or_404(db.select(Record).filter_by(album=album))
            return schema(rec)

        if genre:
            rec = db.first_or_404(db.select(Record).filter_by(genre=genre))
            return schema(rec)

        return Record.query.all()

    def post(self):
        try:
            rec = Record(band=request.args.get('band'),
                         album=request.args.get('album'),
                         genre=request.args.get(
                'genre') if request.args.get('genre') else None)

            db.session.add(rec)
            db.session.commit()

            return schema(rec)

        except Exception:
            return {"error": "error"}, 500

    def delete(self):
        pass
