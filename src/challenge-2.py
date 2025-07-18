# Challenge 2 – Pandas: Exploratory Analysis using Pandas

### Tasks:

## 1. Load the data with Pandas, and create a new column called `dias_desde_ultima_compra` (assuming current date = "2025-07-17").

## 2. Create a boolean column `possivel_churn`, which is True if the customer hasn’t made a purchase in the last 180 days.

## 3. Calculate the average `total_gasto` for clients marked as `possivel_churn == True`.

import numpy as np
import pandas as pd
from datetime import date

df = pd.read_csv("sample_data/clientes.csv", parse_dates=["data_entrada", "data_ultima_compra"])

dias_desde_ultima_compra = pd.to_datetime(date.today()) - pd.to_datetime(df['data_ultima_compra'])

df['possivel_churn'] = dias_desde_ultima_compra.dt.days > 180

df_churned = df[df['possivel_churn'] == True]

media_churn = df_churned['total_gasto'].sum() / df_churned.shape[0]

print(f"Média Churn clientes: {media_churn}")