import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# conf
ruta_csv = "/Users/carcerezo/Desktop/TFG/DATASET/bigrama_tfidf_corregido.csv"
ruta_salida = "/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales"
os.makedirs(ruta_salida, exist_ok=True)

# carga
df = pd.read_csv(ruta_csv)
df["tfidf"] = pd.to_numeric(df["tfidf"], errors="coerce")
df["año"] = df["año"].astype(int)

# quitar bigramas tipicos
stop_bigrams = {
    "federal reserve", "federal funds", "monetary policy",
    "open market", "funds rate", "target range",
    "board governors", "reserve bank", "participants noted",
    "labor market", "division monetary", "monetary affairs",
    "director division", "federal open"
}

df_filtrado = df[~df["bigrama"].isin(stop_bigrams)]

#  top 10 x año 
df_top = df_filtrado.groupby("año").apply(lambda g: g.nlargest(10, "tfidf")).reset_index(drop=True)

# visualizacion
plt.figure(figsize=(12, 8))
sns.barplot(data=df_top, x="año", y="tfidf", hue="bigrama")
plt.title("Top 10 bigramas distintivos por año (TF-IDF filtrado)")
plt.ylabel("Valor TF-IDF")
plt.xlabel("Año")
plt.legend(title="Bigrama", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{ruta_salida}/10_tfidf_filtrado_bigrama_por_anio.png")
plt.close()

print(" Gráfico generado y guardado sin bigramas estructurales.")
