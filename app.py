from src import app, db_init
from src.models import Models

def create_app()
    models = Models()
    models.initialize()
    db_init.init_database('src/data.sql', models)
    return app
