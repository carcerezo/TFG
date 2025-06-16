import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# CSV
df = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_mensual.csv')
df["año_mes"] = pd.to_datetime(df["año_mes"])

# carpeta de salida
output_dir = '/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales'
os.makedirs(output_dir, exist_ok=True)

# crear grafico
plt.figure(figsize=(14, 6))
plt.plot(df["año_mes"], df["sentimiento_textblob"], marker='o', linestyle='-', color='indigo')
plt.title("Evolución del Sentimiento Mensual en Discursos del FOMC (TextBlob)", fontsize=14)
plt.xlabel("Mes")
plt.ylabel("Sentimiento (TextBlob)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# guardar grafico
plt.savefig(os.path.join(output_dir, 'grafico_sentimiento_mensual.png'), dpi=300)
