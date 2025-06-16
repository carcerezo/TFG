import pandas as pd
import matplotlib.pyplot as plt

# cargar sentimiento mensual
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_mensual.csv')
df_sent['año_mes'] = pd.to_datetime(df_sent['año_mes'])

# cargar sp500
df_sp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/HistoricalData_S&P500.csv')
df_sp.rename(columns={'Fecha': 'fecha', 'Cerrar/último': 'cierre'}, inplace=True)
df_sp['fecha'] = pd.to_datetime(df_sp['fecha'], errors='coerce')
df_sp = df_sp.dropna(subset=['fecha'])
df_sp['cierre'] = df_sp['cierre'].astype(str).str.replace(',', '', regex=False).astype(float)
df_sp['año_mes'] = df_sp['fecha'].dt.to_period('M').dt.to_timestamp()

# agrupar sp500 x mes
df_sp_mensual = df_sp.groupby('año_mes')['cierre'].mean().reset_index()

# unir con sentimiento mensual
df_merged = pd.merge(df_sent, df_sp_mensual, on='año_mes', how='inner')

# normalizar
df_merged['sent_norm'] = (df_merged['sentimiento_textblob'] - df_merged['sentimiento_textblob'].min()) / (df_merged['sentimiento_textblob'].max() - df_merged['sentimiento_textblob'].min())
df_merged['sp_norm'] = (df_merged['cierre'] - df_merged['cierre'].min()) / (df_merged['cierre'].max() - df_merged['cierre'].min())

# grafica
plt.figure(figsize=(12, 6))
plt.plot(df_merged['año_mes'], df_merged['sent_norm'], label='Sentimiento (normalizado)', marker='o')
plt.plot(df_merged['año_mes'], df_merged['sp_norm'], label='S&P 500 (normalizado)', marker='o')
plt.title('Evolución mensual: Sentimiento vs S&P 500')
plt.xlabel('Mes')
plt.ylabel('Valores normalizados')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales/sentimiento_vs_sp500_mensual.png')
plt.close()
