from flask import Flask
from flask_cors import CORS
from .config import config
from .exts import toolbar

from app.index import bp as index_bp
from app.kits import bp as kits_bp
from app.api.v_1_0 import bp as v_1_0_bp


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    app.register_blueprint(index_bp)
    app.register_blueprint(kits_bp)
    app.register_blueprint(v_1_0_bp)

    if config_name=="development":
        toolbar.init_app(app)
    # CORS(app, resources=r'/api/*')

    return app
