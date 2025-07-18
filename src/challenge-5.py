# Desafio 3 – Detectar Duplicatas e Corrigir Dados
# Você recebeu um arquivo de leads de marketing com erros.

# Tarefas:
# 1. Identifique e remova registros duplicados baseando-se no email.

# 2. Padronize os nomes para título (ex: Ana, Bruno Lima) usando .str.title().

# 3. Verifique se há datas inválidas ou faltantes.

import pandas as pd

leads_df = pd.read_csv("sample_data/leads.csv")

leads_cleaned = leads_df.groupby('email').agg({
    'nome': 'first',
    'data_inscricao': 'first'
})

leads_cleaned['nome'] = leads_cleaned['nome'].str.title()
leads_cleaned = leads_cleaned.dropna(subset=['data_inscricao'])

leads_cleaned.head()