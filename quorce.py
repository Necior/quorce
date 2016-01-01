#!/usr/bin/env python3

import datetime
import sqlite3
from contextlib import closing
from flask import Flask, g, render_template, redirect, request, url_for
from flask.ext.misaka import Misaka

app = Flask(__name__)
Misaka(app)
app.url_map.strict_slashes = False
app.config.from_object('config')


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'],
                         detect_types=sqlite3.PARSE_DECLTYPES)
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/add_quote', methods=['POST'])
def add_quote():
    if request.form['password'] == app.config['PASSWORD']:
        now = datetime.datetime.now()
        g.db.execute(
                'insert into quotes (text, source, datetime) values (?, ?, ?)',
                (request.form['text'], request.form['source'], now))
        g.db.commit()
    return redirect(url_for('list_quotes'))


@app.route('/')
def list_quotes():
    cur = g.db.execute(
            'select id, text, source, datetime from quotes order by id desc')
    quotes = cur.fetchall()
    return render_template('home.html', quotes=quotes)


@app.route('/quote/<int:id>')
def show_quote(id):
    cur = g.db.execute(
            'select id, text, source, datetime from quotes where id=?', (id,))
    quote = cur.fetchone()
    return render_template('quote.html', q=quote)


@app.route('/preview', methods=['POST'])
def preview_quote():
    quote = {'text': request.form['text'],
             'source': request.form['source'],
             'datetime': datetime.datetime.now(),
             }
    return render_template('quote.html', q=quote)


if __name__ == '__main__':
    app.run()
