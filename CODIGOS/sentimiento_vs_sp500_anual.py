import pandas as pd
import matplotlib.pyplot as plt

# cargar sentimiento anual
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_anual.csv')  # Cambia la ruta si es necesario

# cargar datos sp500
df_sp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/HistoricalData_S&P500.csv')
df_sp.rename(columns={'Fecha': 'fecha', 'Cerrar/último': 'cierre'}, inplace=True)
df_sp['fecha'] = pd.to_datetime(df_sp['fecha'], errors='coerce')
df_sp = df_sp.dropna(subset=['fecha'])
df_sp['cierre'] = df_sp['cierre'].astype(str).str.replace(',', '', regex=False).astype(float)
df_sp['año'] = df_sp['fecha'].dt.year

# agrupar por año
df_sp_anual = df_sp.groupby('año')['cierre'].mean().reset_index()

# unir sentimiento y sp500
df_merged = pd.merge(df_sent, df_sp_anual, on='año', how='inner')

# normalizar 
df_merged['sent_norm'] = (df_merged['sentimiento_medio_anual'] - df_merged['sentimiento_medio_anual'].min()) / (df_merged['sentimiento_medio_anual'].max() - df_merged['sentimiento_medio_anual'].min())
df_merged['sp_norm'] = (df_merged['cierre'] - df_merged['cierre'].min()) / (df_merged['cierre'].max() - df_merged['cierre'].min())

# graficas
plt.figure(figsize=(10, 6))
plt.plot(df_merged['año'], df_merged['sent_norm'], marker='o', label='Sentimiento (normalizado)')
plt.plot(df_merged['año'], df_merged['sp_norm'], marker='o', label='S&P 500 (normalizado)')
plt.title('Evolución anual: Sentimiento vs. S&P 500')
plt.xlabel('Año')
plt.ylabel('Valores normalizados')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales/sentimiento_vs_sp500_anual.png')
plt.close()
