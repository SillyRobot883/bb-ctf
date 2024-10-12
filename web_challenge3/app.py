from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Hardcoded credentials
correct_username = "admin"
correct_password = "s3cr3tP@ssw0rd"

# Retrieve flag from environment variable
flag = os.getenv("FLAG")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == correct_username and password == correct_password:
            return f"Flag: {flag}"
        else:
            return "Login failed. Try again."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
