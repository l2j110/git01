from flask import Flask, render_template
import sqlite3
import os




app = Flask(__name__)

@app.route("/")
def main_page():
    # conn = sqlite3.connect('info.db')
    # cur = conn.cursor()
    # cur.execute("select price, product from member")
    # rows = cur.fetchall()
    # conn.close()

    return render_template("index1.html")

@app.route("/delete/<id>")
def delete():
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute('delete ')


app.run(host='0.0.0.0', debug=True, port=8002)