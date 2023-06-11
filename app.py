from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True

def connect_db():
    sql = sqlite3.connect('./data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_bd():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        
        db = get_bd()
        db.execute('insert into users (name, location) values (?, ?)', [name, location])
        db.commit()

        return redirect(url_for('home', name=name, loc=location))

@app.route('/home/<name>/<loc>')
def home(name, loc):
    isDisplay = name=='Yuqi'
    return render_template('home.html',
                           name=name, 
                           loc=loc, 
                           isDisplay=isDisplay,
                           menu=['Noodle', 'Rice', 'Burger', 'Steak'])

@app.route('/viewresults')
def viewresults():
    db = get_bd()
    cur = db.execute('select id, name, location from users')
    results = cur.fetchall()
    # return '<h1>The ID is {}. The name is {}. The location is {} </h1>'.format(results[0]['id'], results[0]['name'], results[0]['location'])
    # return '<h1>The ID is {}. The name is {}. The location is {} </h1>'.format(results[1]['id'], results[1]['name'], results[1]['location'])
    return '<h1>The ID is {}. The name is {}. The location is {} </h1>'.format(results[2]['id'], results[2]['name'], results[2]['location'])