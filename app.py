from flask import Flask, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/get-location', methods=['GET'])
def get_location():
    api_url = 'https://api.ip2location.io/?key=8DBEB1CD87E525D0C3A64AABCC04D077&ip=116.99.6.135'
    response = requests.get(api_url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Không thể lấy dữ liệu từ API"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))  # Glitch yêu cầu PORT=3000
    app.run(host='0.0.0.0', port=port)
