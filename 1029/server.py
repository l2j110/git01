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
        created_at timestamp default current_timestamp)
        ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def index():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select id, name, phone, address, course from member order by id DESC")
    rows = cur.fetchall()#                                           정렬         역순
    conn.close()

    return render_template('index.html', rows=rows)

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

@app.route("/delete/<int:mid>", methods=['POST'])
def delete(mid):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE from member where id=?", (mid,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

init_db()
app.run(host=('0.0.0.0'), port=8002, debug=True)