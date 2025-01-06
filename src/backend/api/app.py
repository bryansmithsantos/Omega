from flask import Flask, jsonify, request, abort
import os
import logging
from src.backend.Config import MODEL_PATH  # Configuração do caminho do modelo
from src.backend.Model import load_model  # Função para carregar o modelo
from src.backend.Predict import make_prediction  # Função de previsão
from src.backend.Utils import validate_input  # Função utilitária de validação

# Configuração do logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Variável para armazenar o modelo carregado
model = None

def initialize_model():
    """
    Função para inicializar o modelo de linguagem.
    """
    global model
    try:
        logging.info("Carregando o modelo de linguagem...")
        model = load_model(MODEL_PATH)
        logging.info("Modelo carregado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao carregar o modelo: {e}")
        raise RuntimeError("Falha ao carregar o modelo.")

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificar a saúde da API.
    """
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint para fazer previsões.
    """
    try:
        if not request.is_json:
            abort(400, description="Request must be JSON")

        data = request.get_json()

        # Valida os dados de entrada
        validate_input(data)

        # Realiza a previsão usando a lógica em Predict.py
        prediction = make_prediction(model, data)

        return jsonify(prediction), 200

    except ValueError as ve:
        logging.error(f"Erro de validação: {ve}")
        abort(400, description=str(ve))

    except Exception as e:
        logging.error(f"Erro durante a previsão: {e}")
        abort(500, description="Internal server error during prediction")

@app.errorhandler(400)
def bad_request(error):
    """
    Handler customizado para erros 400.
    """
    return jsonify({"error": error.description}), 400

@app.errorhandler(500)
def internal_error(error):
    """
    Handler customizado para erros 500.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Inicializa o modelo ao iniciar o servidor
    initialize_model()

    # Obtém a porta do ambiente ou usa a porta 5000 por padrão
    port = int(os.environ.get('PORT', 5000))

    # Executa a aplicação Flask com a configuração de debug ativada
    app.run(host='0.0.0.0', port=port, debug=True)