from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        print(name, location)
        return redirect(url_for('home', name=name, loc=location))

@app.route('/home/<name>/<loc>')
def home(name, loc):
    isDisplay = name=='Yuqi'
    return render_template('home.html',name=name, loc=loc, isDisplay = isDisplay)