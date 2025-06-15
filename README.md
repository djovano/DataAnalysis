# DataAnalysis

Projeto de Ciência de Dados

## Tecnologias
- Python 3.11+
- Pandas
- Git/Github
- SQLite
- DBeaver
- Matplotlib
- Plotly
- Scikit-learn

## Como executar o projeto
1. Crie o ambiente virtual python e instale as dependências do projeto:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux ou MacOS
source .venv/bin/activate
pip install -r requirements.txt
2. Execute o script `etl.py` (caso queira processar os dados)
3. Para análise gráfica, execute o script `analyze.py`
4. Para análise estatística (com regressão linear simples), execute o script `predict.py`
```

## Problema de Negócio
O ONU deseja saber quais lugares que mais produzem trigo na África para poder criar um projeto de racionalização de alimentos que possa abastecer todo o Continente.

## Requisitos de negócio
* Coletar dados de produção de trigo na África.
* Analisar os dados, identificando quais países mais produzem trigo.
* Criar um modelo preditivo para prever a quantidade de trigro produzida nos próximos anos, utilizando técnicas de análise estatística.

## Referências
https://www.kaggle.com/datasets/muhammadatiflatif/africa-wheat-production-data-19612025?resource=download