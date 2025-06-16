import pandas as pd
import matplotlib.pyplot as plt

# cargar CSV anual
ruta = '/Users/carcerezo/Desktop/TFG/sentimiento_anual.csv'
df = pd.read_csv(ruta)

#  grafica
plt.figure(figsize=(10, 6))
plt.plot(df["año"], df["sentimiento_medio_anual"], marker='o', color='teal', linewidth=2)
plt.title("Evolución del Sentimiento Medio Anual en Discursos del FOMC (TextBlob)", fontsize=14)
plt.xlabel("Año")
plt.ylabel("Sentimiento Medio Anual (TextBlob)")
plt.grid(True)
plt.xticks(df["año"])
plt.tight_layout()

# guardar 
plt.savefig('/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales/grafico_sentimiento_anual.png', dpi=300)

plt.show()
