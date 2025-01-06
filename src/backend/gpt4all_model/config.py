import os

# Diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models')  # Caminho onde o modelo é salvo e carregado
PARAMS_FILE = os.path.join(MODEL_DIR, 'api.json')  # Caminho do arquivo de parâmetros
LOGS_DIR = os.path.join(BASE_DIR, 'logs')  # Diretório de logs

# Configurações do servidor Flask
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

# Configurações do modelo
MODEL_PATH = os.getenv('MODEL_PATH', os.path.join(MODEL_DIR, 'model.bin'))  # Caminho do modelo, padrão .bin
DEFAULT_MODEL_PARAMS = {
    'temperature': 0.7,
    'top_p': 0.95,
    'top_k': 40,
    'max_tokens': 200,
    'presence_penalty': 0.0,
    'frequency_penalty': 0.0,
    'stop_sequences': [],
    'repeat_penalty': 1.1
}

# Log de erros
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')  # Padrão de log para a aplicação

# Configurações específicas de treinamento e execução do modelo
TRAINING_BATCH_SIZE = int(os.getenv('TRAINING_BATCH_SIZE', 32))
TRAINING_EPOCHS = int(os.getenv('TRAINING_EPOCHS', 5))
LEARNING_RATE = float(os.getenv('LEARNING_RATE', 1e-5))

# Função para garantir que todos os diretórios existam
def ensure_directories():
    """
    Garante que os diretórios necessários existam.
    """
    os.makedirs(MODEL_DIR, exist_ok=True)
    os.makedirs(LOGS_DIR, exist_ok=True)