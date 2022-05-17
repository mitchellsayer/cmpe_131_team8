from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message
from os.path import join, dirname, realpath

# Create database handler
db = SQLAlchemy()

# Create mail handler
mail = Mail()

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images/')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Automatically detected when FLASK_APP env var is set
# App factory pattern.
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'mitchell4408@gmail.com'
    app.config['MAIL_PASSWORD'] = 'lskyjuxllavzoydz'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['CONFIRMATION_NUMBER_LEN'] = 16

	# Initialize db handler
    db.init_app(app)

    # Initialize mail hanlder
    mail.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    with app.app_context():
        from .models import User, Listing, Purchase
        from .auth import auth as auth_blueprint
        from .main import main as main_blueprint

        @login_manager.user_loader
        def load_user(user_id):
            # user_id is primary key for Users table
            return User.query.get(int(user_id))

        # Blueprint for auth routes
        app.register_blueprint(auth_blueprint)

        # Blueprint for all other routes
        app.register_blueprint(main_blueprint)

        # Create Database Models
        db.create_all()

        return app
