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

Depois é só rodar o `index.html` direto e testar :)


## Testes com modelos

Eu adicionei varios modelos para testar qual tem o melhor resultado.

os resultados estão na seção:

  `5. Avaliação`

📊 Comparativo dos Modelos (baseado nos seus resultados):

| Modelo                        | MAE  | RMSE |
| ----------------------------- | ---- | ---- |
| **RandomForestRegressor**     | 2.52 | 2.96 |
| **GradientBoostingRegressor** | 2.64 | 3.14 |
| **XGBRegressor**              | 2.69 | 3.21 |
| **KNeighborsRegressor**       | 2.92 | 3.47 |


PS: Deixei os comentários apenas no RandomForestRegressor, que foi o modelo que usamos para a produção.