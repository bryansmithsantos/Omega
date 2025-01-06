from typing import Dict, Any, Optional
from .model import OmegaModel, ModelParams

class OmegaPredictor:
    def __init__(self, model: OmegaModel):
        self.model = model
    
    def predict(self, 
                prompt: str, 
                params: Optional[Dict[str, Any]] = None,
                stream: bool = False) -> str:
        """
        Realiza uma predição usando o modelo.
        
        Args:
            prompt: O texto de entrada
            params: Parâmetros específicos para esta predição (opcional)
            stream: Se True, retorna a resposta em streaming
            
        Returns:
            O texto gerado pelo modelo
        """
        # Converte os parâmetros se fornecidos
        generation_params = ModelParams.from_dict(params) if params else None
        
        # Gera a resposta
        response = self.model.generate(prompt, params=generation_params)
        
        return response
    
    def adjust_params_for_task(self, task_type: str) -> None:
        """
        Ajusta os parâmetros do modelo para tipos específicos de tarefas.
        
        Args:
            task_type: O tipo de tarefa (ex: 'creative', 'factual', 'code')
        """
        task_params = {
            'creative': {
                'temperature': 0.9,
                'top_p': 0.95,
                'max_tokens': 300,
                'frequency_penalty': 0.5
            },
            'factual': {
                'temperature': 0.3,
                'top_p': 0.85,
                'max_tokens': 150,
                'frequency_penalty': 0.0
            },
            'code': {
                'temperature': 0.5,
                'top_p': 0.9,
                'max_tokens': 500,
                'frequency_penalty': 0.2,
                'stop_sequences': ['\n\n', '```']
            }
        }
        
        if task_type in task_params:
            self.model.update_params(task_params[task_type])
    
    def get_current_params(self) -> Dict[str, Any]:
        """
        Retorna os parâmetros atuais do modelo.
        
        Returns:
            Dicionário com os parâmetros atuais
        """
        return self.model.params.to_dict()

# Exemplo de uso:
def create_predictor(model_path: str, custom_params: Optional[Dict[str, Any]] = None) -> OmegaPredictor:
    """
    Cria um preditor com configurações personalizadas.
    
    Args:
        model_path: Caminho para o arquivo do modelo
        custom_params: Parâmetros personalizados para o modelo (opcional)
        
    Returns:
        Uma instância configurada do OmegaPredictor
    """
    model = OmegaModel(model_path, ModelParams.from_dict(custom_params) if custom_params else None)
    return OmegaPredictor(model)

# Exemplo de como usar:
"""
# Criar um preditor com parâmetros padrão
predictor = create_predictor('caminho/do/modelo')

# Ajustar parâmetros para uma tarefa específica
predictor.adjust_params_for_task('creative')

# Fazer uma predição com parâmetros personalizados
response = predictor.predict(
    prompt="Escreva uma história sobre um robô",
    params={
        'temperature': 0.8,
        'max_tokens': 250
    }
)

# Verificar os parâmetros atuais
current_params = predictor.get_current_params()
"""
