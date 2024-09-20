from flask import Flask, render_template, request, redirect, make_response, url_for, jsonify
import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Simulated user database
users = {}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Disallow registration for specific usernames
        if username.lower() in ["admin", "administrator"]:
            error = "Sorry, we've disabled admin registration at the moment."
        else:
            users[username] = password  # Store user data
            return redirect(url_for('home'))

    return render_template('register.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # Create isAdmin cookie (false by default)
            isAdmin_value = f"{username}:false"
            response = make_response(redirect(url_for('index')))
            response.set_cookie('isAdmin', base64.b64encode(isAdmin_value.encode()).decode())
            return response
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['POST'])
def get_flag():
    isAdmin_cookie = request.cookies.get('isAdmin')
    if isAdmin_cookie:
        decoded_cookie = base64.b64decode(isAdmin_cookie).decode()
        username, is_admin = decoded_cookie.split(":")
        if is_admin.strip() == "true":
            # Get flag from environment variable
            flag = os.getenv('FLAG2')
            return jsonify(flag=flag)
    return jsonify(error="Access denied"), 403

@app.route('/set_admin/<username>')
def set_admin(username):
    # Simulate setting admin for a user (for testing)
    isAdmin_value = f"{username}:true"
    response = make_response(redirect(url_for('index')))
    response.set_cookie('isAdmin', base64.b64encode(isAdmin_value.encode()).decode())
    return response

if __name__ == '__main__':
    app.run(debug=True)
