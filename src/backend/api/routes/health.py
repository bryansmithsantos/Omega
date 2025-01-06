from flask import Blueprint, jsonify

# Criação de um Blueprint para a rota de saúde
health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Verifica a saúde da aplicação.
    Este endpoint geralmente é utilizado para monitoramento de disponibilidade.
    
    Returns:
        Response: JSON com status de saúde da aplicação.
    """
    # Aqui você pode incluir checagens adicionais de status, como banco de dados ou outros serviços.
    return jsonify({"status": "healthy", "message": "API is running smoothly"}), 200