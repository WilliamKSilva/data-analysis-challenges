# Challenge 6 – Conversion Rate by Marketing Channel
# You have the following DataFrame:

# Tasks:
# Calculate the conversion rate per channel (fez_compra == True / visitou_site == True).

# Sort the channels from highest to lowest conversion rate.

# Create a bar chart with the results.

import pandas as pd
import matplotlib.pyplot as plt

canais_df = pd.read_csv("sample_data/canais.csv")

conversao_por_canal = canais_df.groupby('canal_origem').agg({
  'canal_origem': 'first',
  'id_usuario': 'count',
  'visitou_site': 'sum',
  'fez_compra': 'sum'
})
conversao_por_canal.columns = ['canal_origem', 'usuarios', 'visitou_site', 'fez_compra']
conversao_por_canal['taxa_conversao'] = conversao_por_canal['fez_compra'] / conversao_por_canal['usuarios']

conversao = conversao_por_canal.sort_values(by='taxa_conversao', ascending=False)

conversao.set_index('canal_origem')['taxa_conversao'].plot(
    kind='bar', 
    color='skyblue',
    figsize=(10, 6)
)

plt.title('Taxa de Conversão por Canal')
plt.ylabel('Taxa de Conversão (%)')
plt.xlabel('Canal')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.show()