from ct1.src import app
from src.db_init import init_database
from src.models import Models


def create_app():
    models = Models()
    models.initialize()
    init_database('src/data.sql', models)
    return app


application = create_app()
