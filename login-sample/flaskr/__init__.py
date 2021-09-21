# __ init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager() # Flask-Loginライブラリとアプリケーションをつなぐ
# ログインの関数
login_manager.login_view = 'app.login'
# ログインにリダイレクトした際のメッセージ
login_manager.login_message = 'ログインしてください'

config = {
    'development': 'config/development/settings.cfg',
    'production': 'config/production/settings.cfg'
}

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    config_file = config[os.getenv('ENVIROMENT', 'development')]
    app.config.from_pyfile(config_file)
    print(f'config_file = {config_file}')
    from flaskr.views import bp
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app
