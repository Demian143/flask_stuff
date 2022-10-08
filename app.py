from flask import Flask
from flask_restful import Api
from crud import hello_world

app = Flask(__name__)
api = Api(app)


api.add_resource(hello_world.HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
