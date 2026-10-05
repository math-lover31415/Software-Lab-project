import os

from flask import Flask

from app.config import config_by_name

def create_app(env=None):
    app = Flask(__name__)

    env = env or os.environ.get("FLASK_ENV", "development")
    app.config.from_object(config_by_name[env])


    from app.routes.auth_routes import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")

    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    return app
