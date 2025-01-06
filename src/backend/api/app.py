from flask import Flask, jsonify, request, abort
import os
import logging

# Configuração do logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificar a saúde da API.
    Retorna um status 200 com uma mensagem de saúde.
    """
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint para fazer previsões.
    Recebe dados JSON e retorna uma previsão.
    """
    try:
        if not request.is_json:
            abort(400, description="Request must be JSON")

        data = request.get_json()

        if "input_data" not in data:
            abort(400, description="Missing 'input_data' field")

        # Lógica de predição (substitua com o seu modelo)
        prediction = {"prediction": "result_example"}

        return jsonify(prediction), 200

    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        abort(500, description="Internal server error during prediction")

@app.errorhandler(400)
def bad_request(error):
    """
    Custom handler para erros 400 (Bad Request).
    """
    return jsonify({"error": error.description}), 400

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler para erros 500 (Internal Server Error).
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Obtém a porta do ambiente ou usa a porta 5000 por padrão
    port = int(os.environ.get('PORT', 5000))
    
    # Executa a aplicação Flask com a configuração de debug ativada
    app.run(host='0.0.0.0', port=port, debug=True)