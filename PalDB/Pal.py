#! /usr/bin/env python2.7
__author__ = "Adam Richardson"
__Date__ = 18 / 04 / 18

import os
from flask import Flask, render_template, flash, redirect, url_for
from Check import *

# This initiates an instance of the app
app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , palDB.py

# Load default config and override config from an environment variable
# Need to add a secret key otherwise it doesn't know you're unique and throws up errors
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'palDB.db'),
    SECRET_KEY='development key',
))
app.config.from_envvar('PALDB_SETTINGS', silent=True)

# Create a list of palindromes that the user has entered
list_pal = []
# If the list gets greater than 10 then remove the last item
if len(list_pal) > 10:
    del list_pal[9]

# This is then how you specify different routes within the web pages
@app.route('/')
def home():
    return render_template('home.html', palindromes=list_pal)


# Add a route which redirects either adding to the table or removing from table
@app.route('/add', methods=['POST'])
def addPal():
    goodPal = check(list_pal)
    if goodPal:
        flash('New palindrome accepted')
        return redirect(url_for('home'))
    else:
        flash('Sorry, your word was not a palindrome')
        return redirect(url_for('home'))


def data():
    return


if __name__ == '__main__':
    app.run(debug=True)
