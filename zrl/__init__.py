import os
from flask import Flask
from flask_migrate import Migrate
from zrl import views


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    app.register_blueprint(views.bp)

    # Database
    from zrl import database
    app.teardown_appcontext(database.shutdown_session)
    app.cli.add_command(database.init_db_command)
    migrate = Migrate(app, database.db_session)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
