from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
import os
from db_funcs import connect_db, get_db
import sqlite3
from classes import FDataBase
from settings import unicontext, url_maker, secret_key
from forms import feedback_form, login_form


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = secret_key
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

@app.route("/")
def main_page():
    return render_template('main.html', context=unicontext)

@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401) 
    return render_template('profile.html', context=unicontext)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    unicontext['form'] = feedback_form
    if request.method=="POST":
        flash('Сообщение отправлено', category='success')
    return render_template('contact.html', context=unicontext)

@app.route("/login", methods=["GET", "POST"])
def login():
    unicontext['form'] = login_form
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', context=unicontext)


@app.route("/elzhur")
def elzhur():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('elzhur.html', context=unicontext, db=dbase)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()







@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.errorhandler(404)
def not_found(error):
    return render_template('page404.html', context=unicontext), 404

@app.errorhandler(401)
def unauthorized(error):
    return render_template('page401.html', context=unicontext), 401


if __name__ == "__main__":
    app.run(debug=True)