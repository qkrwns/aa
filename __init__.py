from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from . import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    @app.route('/',methods=('GET', 'POST')) # 접속하는 url
    def index():
        data = {"level": 60}
        return data
    # 블루프린트
    # from .views import main_views
    # app.register_blueprint(main_views.bp)

    return app