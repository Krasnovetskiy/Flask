from flask import Flask, request, render_template
from flask_login import LoginManager

login_manager = LoginManager()
app = Flask(__name__)

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

@app.login("/login")
def login():
    return render_template('login.html')

