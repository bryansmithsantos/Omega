from flask import Flask, jsonify
from dotenv import load_load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/predict', methods=['POST'])
def predict():
    # TODO: Implementar lógica de predição
    return jsonify({"message": "Endpoint de predição"})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 