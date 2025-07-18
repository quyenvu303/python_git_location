from flask import Flask, jsonify
import requests
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Kích hoạt CORS cho tất cả các route

@app.route('/get-location', methods=['GET'])
def get_location():
    # API IP2Location
    api_url = 'https://api.ip2location.io/?key=8DBEB1CD87E525D0C3A64AABCC04D077&ip=116.99.6.135'

    # Gửi yêu cầu GET tới API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)  # Trả về dữ liệu JSON cho frontend
    else:
        return jsonify({"error": "Không thể lấy dữ liệu từ API"}), 500


if __name__ == '__main__':
    app.run(debug=True)
