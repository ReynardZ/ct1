from src import app, db_init
from src.models import Models

if __name__ == '__main--':
    models = Models()
    models.initialize()
    db_init.init_database('src/data.sql', models)
    app.run()
