# Challenge 5 – Detect Duplicates and Clean Data
# You received a marketing leads file containing errors.

# Tasks:
# Identify and remove duplicate records based on the email.

# Standardize the names to title case (e.g., Ana, Bruno Lima) using .str.title().

# Check for invalid or missing dates.

import pandas as pd

leads_df = pd.read_csv("sample_data/leads.csv")

leads_cleaned = leads_df.groupby('email').agg({
    'nome': 'first',
    'data_inscricao': 'first'
})

leads_cleaned['nome'] = leads_cleaned['nome'].str.title()
leads_cleaned = leads_cleaned.dropna(subset=['data_inscricao'])

leads_cleaned.head()