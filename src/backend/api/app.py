from flask import Flask, jsonify, request, abort
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if not request.is_json:
            abort(400, description="Request must be JSON")

        data = request.get_json()

        if "input_data" not in data:
            abort(400, description="Missing 'input_data' field")

        prediction = {"prediction": "result_example"}

        return jsonify(prediction), 200

    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        abort(500, description="Internal server error during prediction")

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": error.description}), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)