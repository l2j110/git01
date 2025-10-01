from flask import Flask, request, redirect, render_template
import sqlite3
from calendar import monthrange

app = Flask(__name__)
@app.route("/")
def index():
    # URL 파라미터에서 년도, 월 가져오기
    year = int(request.args.get("year", 2025))
    month = int(request.args.get("month", 10))
    selected_date = request.args.get("date")
    num_days = monthrange(year, month)[1]

    return render_template("calendar.html",
                           year=year,
                           month = month,
                           num_days = num_days,
                           selected_date = selected_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)