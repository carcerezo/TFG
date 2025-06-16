import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np
import os

# cargar sent anual y sp500
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_anual.csv')
df_sp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/HistoricalData_S&P500.csv')

# preprocesar sp500
df_sp.rename(columns={'Fecha': 'fecha', 'Cerrar/último': 'cierre'}, inplace=True)
df_sp['fecha'] = pd.to_datetime(df_sp['fecha'], format='%m/%d/%Y')
df_sp['año'] = df_sp['fecha'].dt.year
df_sp['cierre'] = df_sp['cierre'].astype(str).str.replace(',', '').astype(float)

# valor medio anual sp500
df_sp_anual = df_sp.groupby('año')['cierre'].mean().reset_index()
df_sent['año'] = df_sent['año'].astype(int)

# unir
df_merged = pd.merge(df_sent, df_sp_anual, on='año', how='inner')

# grafico  dispersion + regresion
plt.figure(figsize=(10, 6))
sns.regplot(x='sentimiento_medio_anual', y='cierre', data=df_merged, scatter_kws={"color": "steelblue"}, line_kws={"color": "orange"})
plt.title('Dispersión anual: Sentimiento vs S&P 500')
plt.xlabel('Sentimiento Medio Anual (TextBlob)')
plt.ylabel('S&P 500 (Media Anual)')
plt.grid(True)

# guardar
output_dir = '/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales'
os.makedirs(output_dir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'scatter_sentimiento_vs_sp500_anual.png'), dpi=300)
plt.show()
