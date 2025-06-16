import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.util import ngrams
from collections import Counter
from nltk.corpus import stopwords
import nltk
import os

nltk.download("stopwords")

# ruta
ruta_csv = "/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv"
ruta_guardado = "/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales"
os.makedirs(ruta_guardado, exist_ok=True)

# carga
df = pd.read_csv(ruta_csv)

# filtro bigramas
stop_words = set(stopwords.words("english"))

def filtrar_bigramas(bigramas):
    return [
        (a, b) for a, b in bigramas
        if a.lower() not in stop_words and b.lower() not in stop_words and a.isalpha() and b.isalpha()
    ]

# big globales
texto_completo = " ".join(df["texto_limpio"].astype(str)).lower()
tokens = texto_completo.split()
tokens_filtrados = [word for word in tokens if word.isalpha() and word not in stop_words]

bigramas = list(ngrams(tokens_filtrados, 2))
top_bigrams = Counter(bigramas).most_common(10)

labels = [' '.join(bg) for bg, _ in top_bigrams]
valores = [v for _, v in top_bigrams]

plt.figure(figsize=(10, 6))
sns.barplot(x=valores, y=labels, palette="Blues_d")
plt.title("Top 10 bigramas más frecuentes (2018–2025)")
plt.xlabel("Frecuencia")
plt.ylabel("Bigrama")
plt.tight_layout()
plt.savefig(f"{ruta_guardado}/8_top10_bigrams.png")
plt.close()
print(" Gráfico de bigramas global guardado correctamente.")

# bigframas x año
años = sorted(df["año"].dropna().unique())
for año in años:
    texto_anual = " ".join(df[df["año"] == año]["texto_limpio"].astype(str)).lower()
    tokens_anual = texto_anual.split()
    tokens_filtrados_anual = [w for w in tokens_anual if w.isalpha() and w not in stop_words]
    bigramas_anual = list(ngrams(tokens_filtrados_anual, 2))
    top_bigrams_anual = Counter(bigramas_anual).most_common(10)

    if not top_bigrams_anual:
        continue

    etiquetas = [' '.join(bg) for bg, _ in top_bigrams_anual]
    valores = [v for _, v in top_bigrams_anual]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=valores, y=etiquetas, palette="crest")
    plt.title(f"Top 10 bigramas más frecuentes en {año}")
    plt.xlabel("Frecuencia")
    plt.ylabel("Bigrama")
    plt.tight_layout()
    plt.savefig(f"{ruta_guardado}/8_top10_bigrams_{año}.png")
    plt.close()
    print(f" Gráfico de bigramas para {año} guardado correctamente.")
