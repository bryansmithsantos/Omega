from transformers import GPT2LMHeadModel, GPT2Tokenizer
from config import DEVICE, MAX_LENGTH

def chat_with_model():
    # Carregar o modelo e o tokenizer
    model = GPT2LMHeadModel.from_pretrained("./chat_model")
    tokenizer = GPT2Tokenizer.from_pretrained("./chat_model")
    model.to(DEVICE)

    print("Bem-vindo ao chat com GPT-2! Digite 'sair' para encerrar.")

    # Loop de conversa
    conversation_history = ""
    while True:
        user_input = input("Usuário: ")
        if user_input.lower() == "sair":
            break

        # Adicionar a entrada do usuário ao histórico
        conversation_history += f"Usuário: {user_input}\nIA:"

        # Tokenizar a conversa
        inputs = tokenizer(conversation_history, return_tensors="pt", truncation=True, max_length=MAX_LENGTH).to(DEVICE)

        # Gerar resposta
        output = model.generate(
            inputs["input_ids"],
            max_length=MAX_LENGTH,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
            temperature=0.7,
            top_k=50,
            top_p=0.9
        )

        # Decodificar e exibir a resposta
        response = tokenizer.decode(output[0], skip_special_tokens=True).split("IA:")[-1].strip()
        print(f"IA: {response}")

        # Atualizar o histórico
        conversation_history += f" {response}\n"

if __name__ == "__main__":
    chat_with_model()
