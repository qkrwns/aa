from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


from . import config

db = SQLAlchemy()
migrate = Migrate()

"""
GET /losts
GET /losts/3
POST /losts
PATCH /losts/3
DELETE /losts/3
"""

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.debug = True

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .views import main_views
    app.register_blueprint(main_views.bp)

    CORS(app)
    return app

