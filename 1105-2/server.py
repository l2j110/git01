

from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for
import os
# 얘는 뭐 그냥 파일, 디랙토리 만들 때 쓰는 거

app = Flask(__name__)
DIRS = 'uploads'
os.makedirs(DIRS, exist_ok=True)
# 존재하지 않으면 만드쉐여

@app.route('/')
def up():
    return render_template('up.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'fname' not in request.files:
        return jsonify({'error':'No File Part'}), 400

    file = request.files['fname']

    if file.filename == '':
        return  jsonify({'error':'No Selected File'}), 400

    file_path = os.path.join(DIRS, file.filename)
    file.save(file_path)
    return redirect(url_for("up"))

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(DIRS, filename)
    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"error":"File Not Found"})

@app.route("/list", methods = ['GET'])
def list():
    files = os.listdir(DIRS)
    list = [f for f in files]
    return jsonify(list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5300, debug=True)
