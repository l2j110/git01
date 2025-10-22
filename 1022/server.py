import os
import sqlite3
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
def get_conn():
    return sqlite3.connect('info.db')
def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
    create table if not exists member(
        id integer primary key autoincrement,
        name text not null, 
        phone text, 
        address text, 
        course text, 
        created_at timestamp default (DATETIME('now', 'localtime'))
        ''')
    conn.close()
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    name = (request.form.get('name') or '').strip()
    phone = (request.form.get('phone') or '').strip()
    address = (request.form.get('address') or '').strip()
    course = (request.form.get('course') or '').strip()

    if name:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO member(name, phone, address, course) values (?, ?, ?, ?)",
                    (name, address, phone, course)
                    )
        conn.commit()
        conn.close()

    return redirect(url_for('index'))


init_db()
app.run(host=('0.0.0.0'), port=8002, debug=True)