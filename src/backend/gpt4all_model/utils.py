import os
import logging
import json
from typing import Any, Dict
from datetime import datetime

# Configuração do logging
logging.basicConfig(level=logging.INFO)

def ensure_directory_exists(path: str) -> None:
    """
    Garante que o diretório especificado existe.
    Se não existir, cria o diretório.
    
    Args:
        path (str): Caminho do diretório a ser verificado/criado.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Diretório criado: {path}")
    else:
        logging.info(f"O diretório já existe: {path}")

def save_to_json(data: Dict[str, Any], file_path: str) -> None:
    """
    Salva um dicionário em formato JSON em um arquivo.
    
    Args:
        data (dict): Dados a serem salvos no arquivo.
        file_path (str): Caminho do arquivo onde os dados serão salvos.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Dados salvos em {file_path}")
    except Exception as e:
        logging.error(f"Erro ao salvar dados em {file_path}: {str(e)}")

def load_from_json(file_path: str) -> Dict[str, Any]:
    """
    Carrega dados de um arquivo JSON para um dicionário.
    
    Args:
        file_path (str): Caminho do arquivo JSON a ser carregado.
        
    Returns:
        dict: Dados carregados do arquivo.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            logging.info(f"Dados carregados de {file_path}")
            return data
        except Exception as e:
            logging.error(f"Erro ao carregar dados de {file_path}: {str(e)}")
            return {}
    else:
        logging.warning(f"O arquivo {file_path} não foi encontrado.")
        return {}

def log_error(message: str, exception: Exception) -> None:
    """
    Loga um erro detalhado com mensagem e exceção.
    
    Args:
        message (str): Mensagem de erro.
        exception (Exception): Exceção gerada.
    """
    logging.error(f"{message}: {exception}")

def get_timestamp() -> str:
    """
    Retorna o timestamp atual no formato YYYY-MM-DD_HH-MM-SS.
    
    Returns:
        str: Timestamp atual formatado.
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def validate_params(params: Dict[str, Any], expected_params: Dict[str, type]) -> bool:
    """
    Valida se os parâmetros fornecidos estão de acordo com os tipos esperados.
    
    Args:
        params (dict): Parâmetros a serem validados.
        expected_params (dict): Parâmetros esperados e seus tipos.
        
    Returns:
        bool: True se os parâmetros forem válidos, False caso contrário.
    """
    for param, expected_type in expected_params.items():
        if param not in params:
            logging.warning(f"Parâmetro ausente: {param}")
            return False
        if not isinstance(params[param], expected_type):
            logging.warning(f"Parâmetro inválido: {param}. Esperado: {expected_type}, mas foi recebido: {type(params[param])}")
            return False
    return True