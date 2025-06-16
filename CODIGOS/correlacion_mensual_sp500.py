import pandas as pd
from scipy.stats import pearsonr, spearmanr

# cargar sentimiento mensual
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_mensual.csv')
df_sent['fecha'] = pd.to_datetime(df_sent['fecha'])

# cargar sp500
df_sp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/HistoricalData_S&P500.csv')
df_sp.rename(columns={'Fecha': 'fecha', 'Cerrar/último': 'cierre'}, inplace=True)
df_sp['fecha'] = pd.to_datetime(df_sp['fecha'], errors='coerce')
df_sp = df_sp.dropna(subset=['fecha'])  # Eliminar fechas inválidas
df_sp['cierre'] = df_sp['cierre'].astype(str).str.replace(',', '', regex=False).astype(float)

# unir x fecha
df_merge = pd.merge(df_sent, df_sp, on='fecha', how='inner')

print("\n🔍 Todos los discursos emparejados:")
print(df_merge[['fecha', 'sentimiento_textblob', 'cierre']])

# guardar datos
df_merge.to_csv('/Users/carcerezo/Desktop/TFG/DATASET/resultados_correlacion_mensual_sp500.csv', index=False)

# correlaciones
pearson_corr, _ = pearsonr(df_merge['sentimiento_textblob'], df_merge['cierre'])
spearman_corr, _ = spearmanr(df_merge['sentimiento_textblob'], df_merge['cierre'])

# guardar correlaciones
print(f'\n Correlación de Pearson (mismo día): {pearson_corr:.4f}')
print(f' Correlación de Spearman (mismo día): {spearman_corr:.4f}')

with open('/Users/carcerezo/Desktop/TFG/DATASET/correlaciones_sp500.txt', 'w') as f:
    f.write(f'Correlación de Pearson (mismo día): {pearson_corr:.4f}\n')
    f.write(f'Correlación de Spearman (mismo día): {spearman_corr:.4f}\n')
