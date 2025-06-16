import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ruta
ruta_csv = "/Users/carcerezo/Desktop/TFG/DATASET/bigrama_tfidf_corregido.csv"
ruta_salida = "/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales"
os.makedirs(ruta_salida, exist_ok=True)

# CSV
df = pd.read_csv(ruta_csv)

# convertir numerico 
df["tfidf"] = pd.to_numeric(df["tfidf"], errors="coerce")

# eliminar filas vacias
df = df.dropna(subset=["tfidf", "año", "bigrama"])
df["año"] = df["año"].astype(int)
df["bigrama"] = df["bigrama"].astype(str)

# top 10 bigramas x año tfidf
df_top = df.groupby("año").apply(lambda g: g.nlargest(10, "tfidf")).reset_index(drop=True)

# grafico
plt.figure(figsize=(12, 8))
sns.barplot(data=df_top, x="año", y="tfidf", hue="bigrama")
plt.title("Top 10 bigramas por año según TF-IDF")
plt.ylabel("Valor TF-IDF")
plt.xlabel("Año")
plt.legend(title="Bigrama", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig(f"{ruta_salida}/9_tfidf_bigrama_por_anio.png")
plt.close()

print(" Gráfico TF-IDF por año generado y guardado.")
