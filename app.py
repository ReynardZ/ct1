from ct1.src import app
from src.db_init import init_database
from src.models import Models

if __name__ == '__main__':
    models = Models()
    models.initialize()
    init_database('src/data.sql', models)
    app.run()
