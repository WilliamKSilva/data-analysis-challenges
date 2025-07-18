# Challenge 4 – Pandas: Most Sold Products

# You have two DataFrames: `vendas` and `produtos`.

# 1. Merge the tables using `merge`.

# 2. Calculate total sold per product (`quantidade * preco_unitario`).

# 3. List products from most sold to least sold.

import numpy as np
import pandas as pd
from datetime import date

df_vendas = pd.read_csv("sample_data/vendas.csv")
df_produtos = pd.read_csv("sample_data/produtos.csv")

df_vendas_produtos = pd.merge(df_vendas, df_produtos, on="id_produto")

print(df_vendas_produtos)

vendas = df_vendas_produtos.groupby('id_produto').agg({
    'nome_produto': 'first',
    'quantidade': 'sum',
    'preco_unitario': 'first'
})

vendas['total'] = vendas['quantidade'] * vendas['preco_unitario']
result = vendas.sort_values(by='quantidade', ascending=False)

print(result[['nome_produto', 'quantidade', 'total']])