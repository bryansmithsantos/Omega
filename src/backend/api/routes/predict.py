from flask import Blueprint, request, jsonify
from your_model_module import OmegaModel

predict_bp = Blueprint('predict', __name__)

model = OmegaModel(model_path="models/model.bin")

@predict_bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if 'prompt' not in data:
            return jsonify({"error": "O campo 'prompt' é necessário"}), 400

        prompt = data['prompt']
        prediction = model.generate(prompt)

        return jsonify({"prediction": prediction}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500