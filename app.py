from flask import Flask, render_template, redirect, request, jsonify, url_for, flash
import secrets
import boto_utils
from local_constants import DEPLOYED_GATEWAY
import requests

# necessary for deploying with EBS
app = Flask(__name__)
app.secret_key = secrets.token_hex(128)


# warning: firefox behavior is undetermined. Use chrome for most consistent performance
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    # TODO: change validation to some regex
    valid_url = request.form.get('basic-url')
    try: 
        # will terminate requesting from the website after 3 secs        
        r = requests.get(valid_url, timeout=3) 
        r.raise_for_status()
    except: 
        print('There was an error getting the request')
        flash(u'Misformatted url', 'error')
        return redirect(url_for('home'))
    random_token = secrets.token_urlsafe(7)
    # collision prob = 64**7 = 4.3e12 Nearly impossible collision rate
    # TODO: url timeout and basic auth
    boto_utils.put(valid_url, random_token, 'unimplemented', 'no user field')
    return render_template('home.html', link=DEPLOYED_GATEWAY + random_token)


@app.errorhandler(404)
def page_not_found(_):
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
