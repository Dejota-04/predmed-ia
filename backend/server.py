# Importando funções
from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
import pandas as pd

# Criando a aplicação. A variável app vai conter todo o backend,
# e nós vamos adicionando rotas nela. Cada rota é uma função que
# retorna a página para o front-end.
app = Flask(__name__)

CORS(app)  # Resolve bugs de cross origin

# Carregando o modelo
modelo = pickle.load(open('mlp_previsao_trem.pkl', 'rb'))
print("Modelo carregado", modelo)

# Função para converter horário para minutos
def horario_para_minutos(hora):
    h, m = map(int, hora.split(":"))
    return h * 60 + m

# Função para preencher valores padrão ou calcular as colunas faltantes
def preencher_colunas_faltantes(dia, horario_min):
    # Preenchendo com valores padrão ou cálculos (ajuste conforme necessário)
    return {
        'Lotacao': 50,  # Exemplo: Preencher com valor fixo ou calcular
        'Horario_min': horario_min,
        'Atraso': 5  # Exemplo: Preencher com valor fixo ou calcular
    }

# Definindo rotas (URLs) e associando-as a funções Python

@app.route('/service_status')
def retorna_status():
    return "Server is up!"

@app.route("/prediz_digito", methods=['POST'])
def predict():
    # Pegando o conteúdo do POST em formato JSON
    conteudo_post = request.get_json()

    print(conteudo_post)

    dia = conteudo_post['dia']
    horario = conteudo_post['horario']

    # Convertemos o horário para minutos
    horario_min = horario_para_minutos(horario)
    
    # Preenchendo as colunas faltantes com valores calculados ou padrões
    colunas_faltantes = preencher_colunas_faltantes(dia, horario_min)

    # Criando a entrada para o modelo (simulando a estrutura do modelo)
    entrada = pd.DataFrame({
    'Dia da Semana': [dia],
    'Horario_min': [horario_min],
    'Lotacao': [colunas_faltantes['Lotacao']],
    'Atraso': [colunas_faltantes['Atraso']]
})


    # Fazendo a previsão com o modelo
    previsao = modelo.predict(entrada)

    # Formatar o valor da previsão para exibir em minutos
    previsao_minutos = round(previsao[0])

    print(f"Previsão em minutos: {previsao_minutos}")

    # Retornando a previsão como JSON
    return jsonify({"previsao": previsao_minutos})

if __name__ == "__main__":
    app.run(debug=True)
