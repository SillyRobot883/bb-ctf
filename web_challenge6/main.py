from flask import Flask, request, abort
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Define a simple handler for the root path
@app.route('/')
def index():
    return "The API awaits your command; have you got the key?"

# Define a handler for the /flag endpoint
@app.route('/flag', methods=['GET'])
def flag():
    api_key = request.headers.get("X-API-Key")
    # Hardcoded API key for the challenge
    API_KEY = "9d531987-7e49-45a7-889a-69a84fb7134e"

    if api_key == API_KEY:
        flag = os.getenv("FLAG")
        return f"Here's your flag: {flag}"
    else:
        # If the API key is incorrect, respond with an error message
        abort(401, "Unauthorized")

if __name__ == '__main__':
    port = os.getenv("PORT", 8005)
    app.run(host='0.0.0.0', port=int(port))
