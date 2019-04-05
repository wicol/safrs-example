import logging.config

from flask import Flask
from safrs import SAFRSAPI
from flask_migrate import Migrate
from app.models import db, Thing, SubThing

migrate = Migrate()


def create_api(app, swagger_host=None):
    api = SAFRSAPI(app, host=swagger_host)
    api.expose_object(Thing)
    api.expose_object(SubThing)


def create_app():
    """This app factory omits starting SAFRSAPI to enable running the shell etc in a simpler way"""
    app = Flask("some-api")
    app.config.from_envvar("CONFIG_MODULE")
    logging.config.dictConfig(app.config.get("LOGGING", {}))
    db.init_app(app)
    migrate.init_app(app, db)
    return app


def run_app():
    app = create_app()
    with app.app_context():
        create_api(app, app.config["SWAGGER_HOST"])
    return app
