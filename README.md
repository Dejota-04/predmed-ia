
# PredMED IA – Predição de COVID-19 com Inteligência Artificial

Este projeto utiliza **Machine Learning** para prever a probabilidade de um paciente estar infectado por **COVID-19**, com base em sintomas e fatores de risco. Foi construído com foco em **eventos extremos** de saúde e pode ser integrado a **chatbots** e sistemas de triagem automatizada.

## 📊 Visão Geral

O modelo utiliza uma base de dados com respostas "Sim"/"Não" para diversos sintomas e fatores comportamentais. A partir disso, um classificador de árvore de decisão é treinado para prever a variável alvo: presença ou ausência de COVID-19.

---

## 🧠 Tecnologias e Bibliotecas Utilizadas

- Python 3.x  
- Pandas  
- Scikit-learn  
- Pickle  

---

## ⚙️ Como Funciona

1. **Pré-processamento dos dados**  
   - Remoção de espaços extras
   - Tradução dos nomes de colunas do inglês para o português
   - Codificação das respostas categóricas (Sim/Não) usando `OneHotEncoder`

2. **Treinamento**  
   - Divisão dos dados em treino e teste
   - Treinamento de um modelo `DecisionTreeClassifier`

3. **Avaliação**  
   - Cálculo de acurácia do modelo em dados de teste
   - Exibição da performance em percentual

4. **Persistência**  
   - Salvamento do modelo e do codificador com `pickle`

---

## 📁 Estrutura do Projeto

predmed/
├── modelo/
│ └── covid_model.pkl # Modelo treinado salvo
├── dados/
│ └── Covid_Dataset.csv # Conjunto de dados original
├── notebooks/
│ ├── EDA.ipynb # Análise exploratória
│ └── treino_modelo.ipynb # Pré-processamento + Treinamento
└── README.md

markdown
Copiar
Editar

---

## 📌 Features Utilizadas

As colunas (features) utilizadas no treinamento do modelo são:

- Problema Respiratório  
- Febre  
- Tosse Seca  
- Dor de Garganta  
- Coriza  
- Asma  
- Doença Pulmonar Crônica  
- Dor de Cabeça  
- Doença Cardíaca  
- Diabetes  
- Hipertensão  
- Fadiga  
- Problemas Gastrointestinais  
- Viagem ao Exterior  
- Contato com Paciente COVID  
- Participou de Multidão  
- Visitou Locais Públicos  
- Familiar em Local Público  
- Uso de Máscaras  
- Higienização do Mercado

---

## 🧪 Exemplo de Uso

Após carregar os dados e treinar o modelo, o código exibe:

```bash
Acurácia: 82%
Esse valor representa o percentual de previsões corretas feitas pelo modelo com base nos dados de teste.

📄 Licença
Este projeto é acadêmico, com propósito educativo.
Você pode adaptar e reutilizar para fins pessoais ou de pesquisa.

🙋‍♂️ Autor
Desenvolvido por Dejota (Daniel)
Técnico em Informática | Estudante de TI | Desenvolvedor na Veloon
GitHub: @Dejota-04

yaml
Copiar
Editar

---

Se quiser, posso gerar o arquivo `.md` pronto para você baixar ou subir diretamente pro seu repositório GitHub. Deseja isso?






