from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from crud import hello_world

app = Flask(__name__)


def create_app(app) -> Flask:
    api = Api()
    add_rsc(api)
    api.init_app(app)

    db = SQLAlchemy()
    app_config(app)
    db.init_app(app)

    return app


def app_config(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://aori143:postgres@0.0.0.0:5432/postgres"


def add_rsc(api):
    api.add_resource(hello_world.HelloWorld, '/')


if __name__ == '__main__':
    create_app(app).run()
