import torch

# Nome do modelo base
MODEL_NAME = "gpt2"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Configurações de treinamento
TRAINING_ARGS = {
    "output_dir": "./results",
    "overwrite_output_dir": True,
    "num_train_epochs": 3,
    "per_device_train_batch_size": 4,
    "save_steps": 1000,
    "logging_steps": 500,
    "save_total_limit": 2,
    "logging_dir": "./logs",
    "evaluation_strategy": "steps"
}

# Tamanho máximo de sequência de tokens
MAX_LENGTH = 256
