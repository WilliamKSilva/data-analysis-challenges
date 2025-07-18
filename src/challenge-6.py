# Desafio 4 – Conversão por Canal de Marketing
# Você tem o seguinte DataFrame:

# Tarefas:
# 1. Calcule a taxa de conversão por canal (fez_compra == True / visitou_site == True).

# 2. Ordene os canais da maior para a menor taxa.

# 3. Crie um gráfico de barras com os resultados.

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