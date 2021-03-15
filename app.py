from flask import Flask, render_template, redirect, request, jsonify, url_for
app = Flask(__name__)


@app.route('/')
def server_up():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
