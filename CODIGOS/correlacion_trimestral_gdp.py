import pandas as pd
from scipy.stats import pearsonr, spearmanr

# cargar sentimiento mensual
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_mensual.csv')
df_sent['fecha'] = pd.to_datetime(df_sent['fecha'])
df_sent['trimestre'] = df_sent['fecha'].dt.to_period('Q')

# agrupar x trimestre

df_sent_trimestral = df_sent.groupby('trimestre')['sentimiento_textblob'].mean().reset_index()
df_sent_trimestral['trimestre'] = df_sent_trimestral['trimestre'].dt.to_timestamp()

# cargar PIB
df_pib = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/GDPC1_Historical_Data.csv')
df_pib.columns = ['fecha', 'pib']
df_pib['fecha'] = pd.to_datetime(df_pib['fecha'])

# Unir x trimestre
df_merge = pd.merge(df_sent_trimestral, df_pib, left_on='trimestre', right_on='fecha', how='inner')

# correlaciones
pearson_corr, _ = pearsonr(df_merge['sentimiento_textblob'], df_merge['pib'])
spearman_corr, _ = spearmanr(df_merge['sentimiento_textblob'], df_merge['pib'])

# guardar CSV 
df_merge.to_csv('/Users/carcerezo/Desktop/TFG/DATASET/resultados_correlacion_trimestral_pib.csv', index=False)

# guardar correlaciones
with open('/Users/carcerezo/Desktop/TFG/DATASET/correlaciones_trimestral_gdp.txt', 'w') as f:
    f.write(f'Correlación de Pearson (trimestral): {pearson_corr:.4f}\n')
    f.write(f'Correlación de Spearman (trimestral): {spearman_corr:.4f}\n')


print("\n Correlaciones PIB - Sentimiento (trimestral)")
print(f"Pearson: {pearson_corr:.4f}")
print(f"Spearman: {spearman_corr:.4f}")
