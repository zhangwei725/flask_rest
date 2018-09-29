from flask import Flask

from apps.ext import init_ext
from apps.urls import init_api


def create_app():
    app = Flask(__name__)
    app.debug = True
    init_api(app)
    init_ext(app)
    return app
