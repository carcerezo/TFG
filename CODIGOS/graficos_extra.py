import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.util import ngrams
import nltk

# stopwords
nltk.download('stopwords')

# ruta
ruta_csv = "/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv"
ruta_guardado = "/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales"
os.makedirs(ruta_guardado, exist_ok=True)

# carga
df = pd.read_csv(ruta_csv)
df["fecha"] = df["archivo"].str.extract(r'(\d{8})')[0]
df["fecha"] = pd.to_datetime(df["fecha"], format="%Y%m%d")
df["año"] = df["fecha"].dt.year

orden_anios = list(range(2018, 2026))
colores_anios = {
    2018: "#FF9999", 2019: "#FFCC99", 2020: "#FFFF99", 2021: "#CCFF99",
    2022: "#99FFCC", 2023: "#99CCFF", 2024: "#CC99FF", 2025: "#FF99CC"
}
stopwords_ingles = set(stopwords.words("english"))
texto_completo = " ".join(df["texto_limpio"].astype(str).tolist())

# metricas ad
df["longitud_texto"] = df["texto_limpio"].astype(str).apply(lambda x: len(x.split()))
df["palabras_unicas"] = df["texto_limpio"].astype(str).apply(lambda x: len(set(x.split())))
df["riqueza_lexica"] = df["palabras_unicas"] / df["longitud_texto"]

# nº discursos x año
conteo_anual = df["año"].value_counts().reindex(orden_anios)
plt.figure(figsize=(10,6))
sns.barplot(x=conteo_anual.index, y=conteo_anual.values,
            palette=[colores_anios[a] for a in conteo_anual.index])
plt.title("Número de discursos FOMC por año")
plt.xlabel("Año"); plt.ylabel("Cantidad de discursos")
plt.tight_layout()
plt.savefig(f"{ruta_guardado}/1_numero_discursos.png")
plt.close()

# long media
longitud_media = df.groupby("año")["longitud_texto"].mean().reindex(orden_anios)
plt.figure(figsize=(10,6))
sns.lineplot(x=longitud_media.index, y=longitud_media.values, marker='o', color="black")
for año in orden_anios:
    plt.scatter(año, longitud_media[año], color=colores_anios[año], s=100)
plt.title("Longitud media de discursos por año")
plt.xlabel("Año"); plt.ylabel("Número medio de palabras")
plt.tight_layout()
plt.savefig(f"{ruta_guardado}/2_longitud_media.png")
plt.close()

# riqueza lexica x año
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="año", y="riqueza_lexica", order=orden_anios,
            palette=[colores_anios[a] for a in orden_anios])
plt.title("Riqueza léxica por año")
plt.xlabel("Año"); plt.ylabel("Palabras únicas / total palabras")
plt.tight_layout()
plt.savefig(f"{ruta_guardado}/3_riqueza_lexica.png")
plt.close()

# top 5 palabras
top_palabras_por_año = {}
for año in orden_anios:
    subset = df[df["año"] == año]
    palabras = " ".join(subset["texto_limpio"].astype(str)).split()
    filtradas = [p.lower() for p in palabras if p.lower() not in stopwords_ingles and p.isalpha()]
    top5 = Counter(filtradas).most_common(5)
    top_palabras_por_año[año] = dict(top5)

top_df = pd.DataFrame(top_palabras_por_año).T.fillna(0)
top_df.plot(kind="bar", figsize=(12, 6), colormap="Set2")
plt.title("Top 5 palabras más frecuentes por año (sin stopwords)")
plt.ylabel("Frecuencia"); plt.xlabel("Año")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{ruta_guardado}/4_top5_palabras_por_anio.png")
plt.close()

# top 10 palabras
tokens = texto_completo.split()
tokens_filtradas = [t for t in tokens if t not in stopwords_ingles and len(t) > 3]
frecuencia = Counter(tokens_filtradas).most_common(10)
palabras, valores = zip(*frecuencia)

plt.figure(figsize=(10,6))
sns.barplot(x=valores, y=palabras, palette="Set2")
plt.title("Top 10 palabras más frecuentes (2018–2025)")
plt.xlabel("Frecuencia")
plt.tight_layout()
plt.savefig(f"{ruta_guardado}/5_top10_palabras.png")
plt.close()

# wordcloud
wordcloud = WordCloud(width=1000, height=500, stopwords=stopwords_ingles,
                      background_color="white").generate(texto_completo)
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Nube de palabras más frecuentes (sin stopwords)")
plt.tight_layout()
plt.savefig(f"{ruta_guardado}/6_wordcloud.png")
plt.close()

# frec relativa
palabras_clave = ["inflation", "rate", "growth", "recession"]
uso_palabras = {p: [] for p in palabras_clave}
for año in orden_anios:
    subset = df[df["año"] == año]
    tokens = " ".join(subset["texto_limpio"].astype(str)).split()
    total = len(tokens)
    for palabra in palabras_clave:
        uso_palabras[palabra].append(tokens.count(palabra) / total * 1000)

plt.figure(figsize=(10, 6))
for palabra in palabras_clave:
    plt.plot(orden_anios, uso_palabras[palabra], label=palabra)
plt.title("Frecuencia relativa de palabras clave por año")
plt.xlabel("Año"); plt.ylabel("Frecuencia por mil palabras")
plt.legend()
plt.tight_layout()
plt.savefig(f"{ruta_guardado}/7_frecuencia_palabras_clave.png")
plt.close()

# bigramas
from nltk import ngrams
bigrams = ngrams(texto_completo.split(), 2)
top_bigrams = Counter(bigrams).most_common(10)
labels = [' '.join(bg) for bg, _ in top_bigrams]
valores = [v for _, v in top_bigrams]

plt.figure(figsize=(10,6))
sns.barplot(x=valores, y=labels, palette="Blues_d")
plt.title("Top 10 bigramas más frecuentes (2018–2025)")
plt.xlabel("Frecuencia"); plt.ylabel("Bigrama")
plt.tight_layout()
plt.savefig(f"{ruta_guardado}/8_top10_bigrams.png")
plt.close()
