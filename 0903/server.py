from flask import Flask, render_template

app = Flask(__name__)   # 메인 페이지로 하겠다 뭐 이런 뜻

@app.route("/abc")
def home():
    return render_template('index1.html')


app.run(host='0.0.0.0', port=5400, debug=True)
# 0.0.0.0 이러면 내 아이피 올라옴     실시간으로 서버 수정 가능