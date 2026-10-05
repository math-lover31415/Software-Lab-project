import os

from flask import Flask

from app.config import config_by_name
from app.extensions import socketio


def create_app(env=None):
    app = Flask(__name__)

    env = env or os.environ.get("FLASK_ENV", "development")
    app.config.from_object(config_by_name[env])

    socketio.init_app(app)
    
    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    return app
