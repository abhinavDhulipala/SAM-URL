from flask import Flask, render_template, redirect, request, jsonify, url_for, flash
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(128)

@app.route('/')
def server_up():
    return redirect(url_for('home'))


# warning: firefox behavior is undetermined. Use chrome for most consistent performance
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    # TODO: change validation to some regex
    valid_url = request.form.get('basic-url')
    if not valid_url:
        flash(u'Misformatted url', 'error')
        return redirect(url_for('home'))
    lambda_url = 'deployed arn'
    return render_template('home.html', link=lambda_url)


if __name__ == '__main__':
    app.run(debug=True)
