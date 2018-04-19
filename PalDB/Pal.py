#! /usr/bin/env python2.7
__author__ = "Adam Richardson"
__Date__ = 18 / 04 / 18

import os
import sqlite3
from flask import Flask, render_template, flash, redirect, url_for, g
from Check import *

# This initiates an instance of the app
app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , palDB.py


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    db = get_db()
    with app.open_resource('data.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    # Initializes the database.
    init_db()
    print('Initialized the database.')


@app.teardown_appcontext
def close_db(error):
    # Closes the database again at the end of the request.
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# Load default config and override config from an environment variable
# Need to add a secret key otherwise it doesn't know you're unique and throws up errors
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'palDB.db'),
    SECRET_KEY='development key',
))
app.config.from_envvar('PALDB_SETTINGS', silent=True)


# This is then how you specify different routes within the web pages
@app.route('/')
def home():
    db = get_db()
    cur = db.execute('select title from palindromes')
    pals = cur.fetchall()
    return render_template('home.html', passed=pals)


# Add a route which redirects either adding to the table or removing from table
@app.route('/add', methods=['POST'])
def addPal():
    db = get_db()
    test = check(request.form['palindromes'])
    if test:
        # Make sure db.execute take a string which needs to be accurate
        db.execute('insert into palindromes (title) values (?)', [request.form['palindromes']])
        db.commit()
        flash('New palindrome accepted')
        return redirect(url_for('home'))
    else:
        flash('Sorry, your word was not a palindrome')
        return redirect(url_for('home'))


# Need to add a route which displays the data from the table from the last 10 minutes
@app.route('/display', methods=['GET'])
def display():
    db = get_db()
    cur = db.execute('select title from palindromes order by id desc')
    show = cur.fetchall()
    return render_template('display.html', display_pal=show)


@app.route('/clear', methods=['POST'])
def clear():
    db = get_db()
    db.execute('delete from palindromes')
    db.commit()
    flash('All data cleared, please enter more words')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
