import sqlite3
import os
from settings import secret_key, unicontext
from classes import FDataBase
from flask import Flask, render_template, request, g
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = secret_key

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    #con.row_factory = sqlite3.Row
    return con

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.route("/elzhur")
def elzhur():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('elzhur.html', context=unicontext)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def ins_vals():
    db = connect_db()
    with app.open_resource('ins_vals.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()



if __name__ == "__main__":
    app.run(debug=True)