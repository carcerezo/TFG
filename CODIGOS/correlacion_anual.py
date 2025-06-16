import pandas as pd
from scipy.stats import pearsonr, spearmanr

# cargar sentimiento anual
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_anual.csv')

# cargar PIB
df_pib = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/GDPC1_Historical_Data.csv')
df_pib.columns = ['fecha', 'pib']
df_pib['año'] = pd.to_datetime(df_pib['fecha']).dt.year
df_pib_anual = df_pib.groupby('año')['pib'].mean().reset_index()

# cargar sp500
df_sp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/HistoricalData_S&P500.csv')
df_sp.rename(columns={'Fecha': 'fecha', 'Cerrar/último': 'cierre'}, inplace=True)
df_sp['fecha'] = pd.to_datetime(df_sp['fecha'], errors='coerce')
df_sp = df_sp.dropna(subset=['fecha'])
df_sp['cierre'] = df_sp['cierre'].astype(str).str.replace(',', '', regex=False).astype(float)
df_sp['año'] = df_sp['fecha'].dt.year
df_sp_anual = df_sp.groupby('año')['cierre'].mean().reset_index()

# unir sentimiento con PIB y sp500
df_merge_pib = pd.merge(df_sent, df_pib_anual, on='año', how='inner')
df_merge_sp = pd.merge(df_sent, df_sp_anual, on='año', how='inner')

# correlaciones
pearson_pib, _ = pearsonr(df_merge_pib['sentimiento_medio_anual'], df_merge_pib['pib'])
spearman_pib, _ = spearmanr(df_merge_pib['sentimiento_medio_anual'], df_merge_pib['pib'])

pearson_sp, _ = pearsonr(df_merge_sp['sentimiento_medio_anual'], df_merge_sp['cierre'])
spearman_sp, _ = spearmanr(df_merge_sp['sentimiento_medio_anual'], df_merge_sp['cierre'])

# guardar 
with open('/Users/carcerezo/Desktop/TFG/DATASET/correlaciones_anuales.txt', 'w') as f:
    f.write('Correlación anual PIB - Sentimiento:\n')
    f.write(f'  Pearson: {pearson_pib:.4f}\n')
    f.write(f'  Spearman: {spearman_pib:.4f}\n\n')
    f.write('Correlación anual S&P500 - Sentimiento:\n')
    f.write(f'  Pearson: {pearson_sp:.4f}\n')
    f.write(f'  Spearman: {spearman_sp:.4f}\n')

df_merge_pib.to_csv('/Users/carcerezo/Desktop/TFG/DATASET/resultados_correlacion_anual_pib.csv', index=False)
df_merge_sp.to_csv('/Users/carcerezo/Desktop/TFG/DATASET/resultados_correlacion_anual_sp500.csv', index=False)

print("\n Correlaciones anuales calculadas y guardadas correctamente.")
