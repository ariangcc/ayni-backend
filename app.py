from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app(config_filename):
	app = Flask(__name__)
	app.config.from_object(config_filename)
	app.config['SECRET_KEY'] = 'loconfieso'
	app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="test2", DB_PASS="froz21", DB_ADDR="127.0.0.1", DB_NAME="ayni")
	
	db.init_app(app)
	
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	from models import User

	@login_manager.user_loader
	def load_user(user_id): #Asocia el id de la cookie con el id del user
		return User.query.get(int(user_id))


	from auth import auth as auth_bp
	app.register_blueprint(auth_bp)

	from main import main as main_bp
	app.register_blueprint(main_bp)

	return app
