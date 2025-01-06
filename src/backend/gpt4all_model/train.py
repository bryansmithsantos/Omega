import os
import json
import logging
from flask import Flask, jsonify, request
from omega_model import OmegaModel, ModelParams  # Supondo que OmegaModel esteja em omega_model.py

# Configurações de logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Definir o caminho para o modelo e diretório de salvamento
model_path = "path/to/initial/model"  # Caminho do modelo inicial
save_dir = "path/to/save/directory"  # Diretório onde os dados serão salvos

# Carregar ou criar o modelo
model = OmegaModel(model_path, save_dir)

@app.route('/train', methods=['POST'])
def train_model():
    """
    Endpoint para treinar o modelo com base nos dados fornecidos no corpo da requisição.

    Espera um JSON com um campo 'data' contendo uma lista de strings (dados de treinamento).
    """
    try:
        # Receber dados de treinamento via JSON
        training_data = request.json.get('data')
        if not training_data:
            return jsonify({"error": "Dados de treinamento não fornecidos"}), 400

        # Treinando o modelo
        epochs = request.json.get('epochs', 10)  # Padrão para 10 épocas
        train(model, training_data, epochs)

        return jsonify({"message": "Treinamento concluído e modelo salvo com sucesso!"}), 200
    except Exception as e:
        logging.error(f"Erro durante o treinamento: {e}")
        return jsonify({"error": f"Erro durante o treinamento: {e}"}), 500


@app.route('/update-params', methods=['POST'])
def update_model_params():
    """
    Endpoint para atualizar os parâmetros do modelo com base nos dados fornecidos.
    
    Espera um JSON com os parâmetros a serem atualizados (por exemplo, 'temperature', 'top_p').
    """
    try:
        # Receber os parâmetros a serem atualizados via JSON
        new_params = request.json
        if not new_params:
            return jsonify({"error": "Parâmetros não fornecidos"}), 400

        # Atualizando parâmetros do modelo
        update_model_params_route(model, new_params)

        return jsonify({"message": "Parâmetros do modelo atualizados com sucesso!"}), 200
    except Exception as e:
        logging.error(f"Erro ao atualizar parâmetros: {e}")
        return jsonify({"error": f"Erro ao atualizar parâmetros: {e}"}), 500


@app.route('/generate', methods=['POST'])
def generate_text():
    """
    Endpoint para gerar texto com base no prompt fornecido.
    
    Espera um JSON com um campo 'prompt' contendo o texto de entrada.
    """
    try:
        # Receber prompt de entrada via JSON
        prompt = request.json.get('prompt')
        if not prompt:
            return jsonify({"error": "Prompt não fornecido"}), 400
        
        # Gerando o texto com o modelo
        generated_text = model.generate(prompt)

        return jsonify({"generated_text": generated_text}), 200
    except Exception as e:
        logging.error(f"Erro ao gerar texto: {e}")
        return jsonify({"error": f"Erro ao gerar texto: {e}"}), 500


def train(model: OmegaModel, training_data: list, epochs: int = 10):
    """
    Função de treinamento do modelo OmegaModel.
    
    Args:
        model (OmegaModel): Instância do modelo OmegaModel.
        training_data (list): Dados de treinamento.
        epochs (int): Número de épocas para o treinamento (padrão é 10).
    """
    logging.info(f"Iniciando treinamento com {epochs} épocas.")
    
    # Exemplo de treinamento: apenas simula iteração sobre os dados
    for epoch in range(epochs):
        logging.info(f"Época {epoch + 1}/{epochs} começando...")
        
        # Simula o processo de treinamento
        for i, line in enumerate(training_data):
            # Simula a geração de texto com base na entrada e nos parâmetros
            generated_text = model.generate(line.strip())
            
            # Exemplo de logging durante o treinamento
            if i % 10 == 0:  # Log a cada 10 amostras
                logging.info(f"Exemplo {i+1}: {generated_text}")
        
        # Ao final de cada época, podemos salvar o modelo e parâmetros
        model._save_model()
        logging.info(f"Época {epoch + 1}/{epochs} finalizada. Modelo salvo.")
    
    logging.info("Treinamento completo!")


def update_model_params_route(model: OmegaModel, new_params: dict):
    """
    Atualiza os parâmetros do modelo e salva no arquivo de configuração `api.json`.
    
    Args:
        model (OmegaModel): Instância do modelo OmegaModel.
        new_params (dict): Novo conjunto de parâmetros a ser aplicado ao modelo.
    """
    logging.info(f"Atualizando parâmetros do modelo com: {new_params}")
    model.update_params(new_params)
    logging.info("Parâmetros atualizados e salvos.")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)