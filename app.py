from flask import Flask, request, render_template, session

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
login_manager = LoginManager()

login_manager = LoginManager(app)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'saqaq1q1q1a'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
@app.route("/", methods=['GET', 'POST'])
def index(*args, **kwargs):
    context = {'name': 'Alex'}
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        #logic
        context.update({'name': name, 'password': password})
    return render_template('index.html', **context)

@app.route("/registration", methods=['GET', 'POST'])
def registration():

    return render_template('registration.html')

@app.login('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return print("OK")



    return render_template('login.html')

