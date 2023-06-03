from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return f'<h1>Hello World!<h1>'

@app.route('/home')
def home():
    return f'<h1>This is the homepage!<h1>'