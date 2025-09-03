from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("from.html")

@app.route("/result", methods=['POST'])
def result():
    name=request.form['username']
    print(name)
    return render_template('result.html')


app.run(host='0.0.0.0', port=5500, debug=True)