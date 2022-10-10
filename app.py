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
    from resources import resource
    api.add_resource(resource.QueryAlbum, '/albums/')
    api.init_app(app)


if __name__ == '__main__':
    create_app(app).run()
