from flask import Flask, render_template, redirect, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def server_up():
    return render_template('home.html')


@app.route('/some_info/<int: id>')
def some_info():
    params = request.args
    headers = request.headers
    if not request.is_json:
        return jsonify('not')
    body = request.get_json()
    return jsonify(params=params, headers=headers['testHeader'], body=body, status=201, message='success')


if __name__ == '__main__':
    app.run(debug=True)
