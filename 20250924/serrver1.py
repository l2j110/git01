from flask import Flask, request, render_template

app = Flask(__name__)

PRICES = {
    "pizza" :12000,
    "chicken" : 15000,
    "cola" : 2000,
    "beer" : 4000
}

DISCOUNTS = {
    "none" : 0.0,
    "student" : 0.1,
    "member" : 0.2
}

@app.route('/result', methods=['POST'])
def result():
    menus = request.form.getlist('menu')
    discount = request.form["discount"]

    subtotal = sum(PRICES[m] for m in menus)

    rate = DISCOUNTS[discount]
    total = int(subtotal*(1-rate))

    item_names = [{'pizza' : '피자', 'chicken' : '치킨', 'cola' : '콜라', 'beer' : '맥주'}[m] for m in menus]

    discount_label = {'none' : '없음', 'student' : '학생(10%)', 'member' : '회원(20%)'}[discount]

    return render_template(
        "result.html",
        items = ",".join(item_names) if item_names else '선택 없음',
        discount_label = discount_label,
        total = total
    )

@app.route("/")
def index():
    return render_template("index.html")

app.run(host="0.0.0.0", port=8001, debug=True)