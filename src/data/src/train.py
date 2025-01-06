from transformers import GPT2LMHeadModel, Trainer, TrainingArguments
from prepare_data import prepare_data
from config import MODEL_NAME, DEVICE, TRAINING_ARGS

def train_model(data_file):
    # Preparar os dados
    dataset = prepare_data(data_file)

    # Carregar o modelo GPT-2
    model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
    model.to(DEVICE)

    # Configurações do treinamento
    training_args = TrainingArguments(**TRAINING_ARGS)

    # Criar o Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"]
    )

    # Treinar o modelo
    trainer.train()

    # Salvar o modelo treinado
    model.save_pretrained("./chat_model")
    print("Modelo salvo em './chat_model'")

if __name__ == "__main__":
    train_model("../data/conversa.txt")
