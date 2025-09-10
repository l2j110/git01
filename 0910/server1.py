from flask import render_template,Flask,request

app = Flask(__name__)

FARES = {
    "card" : {"adult": 1500, "teen": 850, "child": 400},
    "cash" : {"adult": 1700, "teen": 1000, "child": 500}
}

@app.route("/result", methods=["POST"])
def result():
    method = request.form["method"]
    age = int(request.form["age"])
    kind = classify(age)
    if kind == "free":
        fare = 0
        label = "무료승차"
    else:
        fare = FARES[method][kind]
        label = {"adult":"성인", "teen":"청소년", "child":"어린이"}[kind]

    return render_template('result.html',
                           method=method,
                           age=age,
                           target=label,
                           fare=fare)



def classify(age: int) -> str:
    if age < 6 or age >= 60:
        return "free"
    if 6 <= age <= 12:
        return "child"
    if 13 <= age <= 18:
        return "teen"
    return "adult"


@app.route("/")
def index():
    return render_template("index.html")

app.run(host='0.0.0.0', port=7300, debug=True)


