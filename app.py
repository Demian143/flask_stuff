from flask import Flask
from flask_restful import Api

app = Flask(__name__)


def create_app(app: Flask) -> Flask:
    init_db(app)
    init_api(app)

    return app


def init_db(app: Flask) -> Flask:
    from db.models import db
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://aori143:postgres@0.0.0.0:5432/postgres"

    db.init_app(app)

    with app.app_context():
        db.create_all()


def init_api(app: Flask):
    api = Api()
    add_resource(api)
    api.init_app(app)


def add_resource(api: Api):
    from resources import resource

    api.add_resource(resource.QueryAlbums, '/albums/')
    api.add_resource(resource.QuerySongs, '/songs/')
    api.add_resource(resource.QueryBands, '/bands/')
    api.add_resource(resource.QueryGenres, '/genres/')


if __name__ == '__main__':
    create_app(app).run()
