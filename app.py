from flask import Flask, render_template, redirect, request, jsonify, url_for, flash
import secrets
import boto_utils
from local_constants import DEPLOYED_GATEWAY
import requests
from urllib3.exceptions import HTTPError

app = Flask(__name__)
app.secret_key = secrets.token_hex(128)


# warning: firefox behavior is undetermined. Use chrome for most consistent performance
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    url = request.form.get('basic-url')
    try:
        not_valid = requests.get(url, timeout=3).status_code != 200
    except requests.exceptions.RequestException:
        not_valid = True
    except HTTPError:
        not_valid = True

    if not_valid:
        flash(u'Misformatted url', 'error')
        return redirect(url_for('home'))
    # TODO: Part 1
    # collision prob = 64**7 = 4.3e12 Nearly impossible collision rate
    return render_template('home.html', link=DEPLOYED_GATEWAY + random_token)


@app.errorhandler(404)
def page_not_found(_):
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
