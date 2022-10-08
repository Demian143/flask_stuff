from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from crud import hello_world

app = Flask(__name__)


def create_app(app) -> Flask:
    api = Api()
    add_rsc(api)
    api.init_app(app)

    # db = SQLAlchemy()
    # db.init_app(app)

    return app


def add_rsc(api):
    api.add_resource(hello_world.HelloWorld, '/')


if __name__ == '__main__':
    create_app(app).run()
