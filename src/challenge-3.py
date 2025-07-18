# Challenge 3 – Pandas: Monthly Revenue Analysis

### Tasks:

## 1. Create a column `mes_ano` in the format "YYYY-MM".

## 2. Calculate total revenue per month.

## 3. Generate a line chart showing monthly revenue evolution.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data/pedidos.csv", parse_dates=["data_pedido"])

df['mes_ano'] = df['data_pedido'].dt.to_period('M')

faturamento_por_mes = df.groupby('mes_ano')['valor_total'].sum()
faturamento_por_mes.plot(kind='line', marker='o')

plt.title('Monthly Revenue')
plt.xlabel('Month-Year')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.show()