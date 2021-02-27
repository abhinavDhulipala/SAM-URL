from flask import Flask, render_template, redirect, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def server_up():
    return render_template('home.html')

@app.route('/some_info')
def some_info():
    params = request.args
    headers = request.headers
    body = json.loads(request.data.decode('utf-8'))
    return jsonify(params=params, headers=headers['testHeader'], body=body, code=200, message='success')


if __name__ == '__main__':
    app.run(debug=True)
