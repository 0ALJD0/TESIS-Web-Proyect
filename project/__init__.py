from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from project.config import Config
from flask_session import Session

sess = Session()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    sess.init_app(app)

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    from .models import Administrador, Establecimiento, Horario  # Importa los modelos aquí para que Alembic los detecte

    return app
