# Predizendo digitos com ML

projeto para praticar conceitos de serialização de modelos, criação de servidores, e treino de redes neurais em python.

O modelo é para a tarefa de predizer dígitos escritos à mão.

-----

Se estiver usando o vscode, instale a extensão de ID `ms-toolsai.jupyter`

## Executando

Primeiro instale as dependências com:

```bash
pip install -r requirements.txt
```

Treine o modelo rodando o notebook `./backend/treina_modelo.ipynb`

Para executar o servidor, abra um terminal na pasta `./backend` e `./run.bat` execute:

```bash
set FLASK_APP=server.py
set FLASK_RUN_PORT=8000
set FLASK_DEBUG=1


flask run
```

