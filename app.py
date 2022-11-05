from src import create_app


<<<<<<< HEAD
=======
def create_app():
    models = Models()
    models.initialize()
    init_database('src/data.sql', models)
    return app


>>>>>>> 0d53d7fa27671234eb553b5c078e61ae222851e8
application = create_app()
