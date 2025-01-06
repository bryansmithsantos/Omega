import os
import json
import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class ModelParams:
    """
    Representa os parâmetros do modelo de aprendizado, que podem ser configurados
    para gerar diferentes resultados de acordo com os valores definidos.

    Attributes:
        temperature (float): Controla a aleatoriedade na geração de texto.
        top_p (float): Parâmetro de "nucleus sampling" que controla a diversidade.
        top_k (int): Número de palavras mais prováveis a serem selecionadas.
        max_tokens (int): Número máximo de tokens gerados na resposta.
        presence_penalty (float): Penalidade aplicada para a presença de palavras no texto.
        frequency_penalty (float): Penalidade aplicada para palavras mais frequentes.
        stop_sequences (Optional[list[str]]): Sequências que, quando geradas, param a resposta.
        repeat_penalty (float): Penalidade para repetições de palavras no texto gerado.
    """
    temperature: float = 0.7
    top_p: float = 0.95
    top_k: int = 40
    max_tokens: int = 200
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0
    stop_sequences: Optional[list[str]] = None
    repeat_penalty: float = 1.1
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte os parâmetros do modelo para um dicionário.

        Returns:
            dict: Dicionário com os parâmetros do modelo.
        """
        return {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "max_tokens": self.max_tokens,
            "presence_penalty": self.presence_penalty,
            "frequency_penalty": self.frequency_penalty,
            "stop_sequences": self.stop_sequences or [],
            "repeat_penalty": self.repeat_penalty
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModelParams":
        """
        Cria uma instância de ModelParams a partir de um dicionário.

        Args:
            data (dict): Dicionário contendo os parâmetros do modelo.

        Returns:
            ModelParams: Instância de ModelParams configurada com os dados fornecidos.
        """
        return cls(
            temperature=data.get("temperature", 0.7),
            top_p=data.get("top_p", 0.95),
            top_k=data.get("top_k", 40),
            max_tokens=data.get("max_tokens", 200),
            presence_penalty=data.get("presence_penalty", 0.0),
            frequency_penalty=data.get("frequency_penalty", 0.0),
            stop_sequences=data.get("stop_sequences", None),
            repeat_penalty=data.get("repeat_penalty", 1.1)
        )


class OmegaModel:
    """
    Representa o modelo de aprendizado, incluindo a lógica para carregar, gerar
    texto e salvar os dados aprendidos em arquivos.

    Attributes:
        model_path (str): Caminho do arquivo do modelo.
        save_dir (str): Diretório onde os arquivos do modelo e parâmetros são salvos.
        params (ModelParams): Parâmetros configurados para o modelo.
        api_file_path (str): Caminho do arquivo onde os dados do modelo são salvos (api.json).
    """
    
    def __init__(self, model_path: str, save_dir: str, params: Optional[ModelParams] = None):
        """
        Inicializa o modelo, carrega os dados e garante que o diretório de salvamento exista.

        Args:
            model_path (str): Caminho para o arquivo do modelo.
            save_dir (str): Caminho para o diretório onde os dados do modelo serão salvos.
            params (Optional[ModelParams]): Parâmetros do modelo (padrão é `ModelParams`).
        """
        self.model_path = model_path
        self.save_dir = save_dir
        self.params = params or ModelParams()
        self.api_file_path = os.path.join(save_dir, "src", "backend", "api", "routes", "api.json")
        self._ensure_directory()
        self._load_model()
    
    def _ensure_directory(self):
        """
        Garante que o diretório de salvamento para o modelo e dados exista.
        Se o diretório não existir, ele será criado.
        """
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
    
    def _load_model(self):
        """
        Carrega o modelo e os parâmetros configurados de arquivos persistidos, incluindo o `api.json`.

        Carrega o modelo e os dados de parâmetros do arquivo JSON se ele existir. Caso contrário, o modelo
        será inicializado com parâmetros padrão.
        """
        try:
            model_file = os.path.join(self.save_dir, "model.bin")
            if os.path.exists(model_file):
                logging.info(f"Modelo carregado de {model_file}")
            else:
                logging.info("Nenhum modelo anterior encontrado. Criando um novo modelo.")
            
            self._load_api_data()
        except Exception as e:
            logging.error(f"Falha ao carregar o modelo: {e}")
            raise RuntimeError("Erro ao carregar o modelo")
    
    def _load_api_data(self):
        """
        Carrega os dados do modelo do arquivo `api.json`.

        O arquivo `api.json` contém os parâmetros do modelo que foram aprendidos ou configurados
        em execuções anteriores.
        """
        if os.path.exists(self.api_file_path):
            try:
                with open(self.api_file_path, "r") as file:
                    api_data = json.load(file)
                    self.params = ModelParams.from_dict(api_data.get("params", {}))
                    logging.info("Dados carregados de api.json.")
            except Exception as e:
                logging.error(f"Erro ao carregar dados de api.json: {e}")
    
    def _save_model(self):
        """
        Salva o modelo e os parâmetros no diretório de salvamento, incluindo no arquivo `api.json`.

        O modelo é simulado como salvo em um arquivo binário e os parâmetros são salvos no formato JSON.
        """
        try:
            model_file = os.path.join(self.save_dir, "model.bin")
            logging.info(f"Modelo salvo em {model_file}")
            
            params_file = os.path.join(self.save_dir, "params.json")
            with open(params_file, "w") as f:
                json.dump(self.params.to_dict(), f)
            logging.info(f"Parâmetros salvos em {params_file}")
            
            api_data = {"params": self.params.to_dict()}
            os.makedirs(os.path.dirname(self.api_file_path), exist_ok=True)
            with open(self.api_file_path, "w") as api_file:
                json.dump(api_data, api_file, indent=4)
            logging.info(f"Dados salvos em {self.api_file_path}")
        except Exception as e:
            logging.error(f"Erro ao salvar o modelo: {e}")
    
    def generate(self, prompt: str, params: Optional[ModelParams] = None) -> str:
        """
        Gera texto baseado no prompt fornecido.

        Args:
            prompt (str): Texto de entrada fornecido ao modelo.
            params (Optional[ModelParams]): Parâmetros personalizados para a geração (opcional).

        Returns:
            str: Texto gerado pelo modelo.
        """
        generation_params = params or self.params
        
        try:
            response = f"Texto gerado com prompt: {prompt} e parâmetros: {generation_params.to_dict()}"
            return response
        except Exception as e:
            logging.error(f"Erro na geração de texto: {e}")
            return "Erro ao gerar texto"

    def update_params(self, new_params: Dict[str, Any]) -> None:
        """
        Atualiza os parâmetros do modelo e os salva no diretório de salvamento, incluindo no arquivo `api.json`.

        Args:
            new_params (Dict[str, Any]): Novos parâmetros a serem aplicados ao modelo.
        """
        current_params_dict = self.params.to_dict()
        current_params_dict.update(new_params)
        self.params = ModelParams.from_dict(current_params_dict)
        self._save_model()  # Salva os parâmetros atualizados no diretório


def create_model(model_path: str, save_dir: str, custom_params: Optional[Dict[str, Any]] = None) -> OmegaModel:
    """
    Cria uma instância do modelo com parâmetros personalizados e define o diretório de salvamento.

    Args:
        model_path (str): Caminho para o arquivo do modelo.
        save_dir (str): Caminho onde os dados do modelo serão salvos.
        custom_params (Optional[Dict[str, Any]]): Parâmetros personalizados para o modelo (opcional).

    Returns:
        OmegaModel: Instância configurada do OmegaModel.
    """
    params = ModelParams.from_dict(custom_params) if custom_params else ModelParams()
    return OmegaModel(model_path, save_dir, params)