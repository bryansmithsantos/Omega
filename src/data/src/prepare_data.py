from datasets import load_dataset
from transformers import GPT2Tokenizer
from config import MODEL_NAME, MAX_LENGTH

def prepare_data(file_path):
    # Carregar o tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)

    # Carregar os dados
    dataset = load_dataset("text", data_files={"train": file_path})

    # Concatenar mensagens de "Usuário" e "IA"
    def format_conversation(examples):
        dialogues = examples["text"].split("\n")
        conversation = " ".join(dialogues).replace("Usuário:", "\nUsuário:").replace("IA:", "\nIA:")
        return {"text": conversation}

    dataset = dataset.map(format_conversation, batched=False)

    # Tokenizar
    def tokenize_function(examples):
        return tokenizer(
            examples["text"],
            truncation=True,
            padding="max_length",
            max_length=MAX_LENGTH
        )

    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    tokenized_dataset.set_format(type="torch", columns=["input_ids", "attention_mask"])
    
    return tokenized_dataset
