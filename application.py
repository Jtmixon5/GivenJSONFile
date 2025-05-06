from flask import Flask, jsonify
import json
import os

# Azure expects a callable named 'application'
app = Flask(__name__)

# Path to the JSON file (adjust if needed)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'GivenData.json')

# Load the JSON data
with open(DATA_FILE) as f:
    data = json.load(f)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Optional root route
@app.route('/')
def index():
    return "Flask API is running. Use /data to get the JSON."

# For local development/testing
if __name__ == '__main__':
    app.run(debug=True)