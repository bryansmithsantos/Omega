# Projeto Omega

Um assistente de IA baseado em GPT4All com interface desktop usando Electron e Python.

## Requisitos

- Python 3.8+
- Node.js 14+
- npm ou yarn

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/omega.git
cd omega
```

2. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

3. Instale as dependências Node.js:
```bash
npm install
```

## Executando o projeto

1. Inicie o backend:
```bash
python src/backend/api/app.py
```

2. Em outro terminal, inicie o frontend:
```bash
npm start
```

## Estrutura do Projeto

O projeto está organizado em:
- `frontend/`: Interface do usuário com Electron
- `backend/`: Servidor Python com o modelo GPT4All
- `models/`: Modelos treinados
- `data/`: Dados de treinamento
- `tests/`: Testes unitários e de integração

## Licença

MIT 