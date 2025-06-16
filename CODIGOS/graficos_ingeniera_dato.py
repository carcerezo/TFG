import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re

# Leer el CSV
ruta_csv = "/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv"
df = pd.read_csv(ruta_csv)

# Calcular longitud del texto
df["longitud_texto"] = df["texto_limpio"].apply(lambda x: len(str(x).split()))

# Extraer el año desde el nombre del archivo por seguridad
df["año"] = df["archivo"].apply(lambda x: re.search(r'20\d{2}', x).group(0) if re.search(r'20\d{2}', x) else None)

# ========== 1. Gráfica de número de discursos por año ==========
conteo_anual = df["año"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
sns.barplot(x=conteo_anual.index, y=conteo_anual.values)
plt.title("Número de discursos FOMC por año (2018–2025)")
plt.xlabel("Año")
plt.ylabel("Cantidad de discursos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ========== 2. Gráfica de longitud promedio por año ==========
longitud_promedio = df.groupby("año")["longitud_texto"].mean()

plt.figure(figsize=(10, 5))
sns.lineplot(x=longitud_promedio.index, y=longitud_promedio.values, marker="o")
plt.title("Longitud promedio de discursos FOMC por año")
plt.xlabel("Año")
plt.ylabel("Número promedio de palabras")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ========== 3. Nube de palabras ==========
texto_completo = " ".join(df["texto_limpio"].dropna().astype(str).tolist())

wordcloud = WordCloud(width=1000, height=500, background_color='white').generate(texto_completo)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Nube de palabras - Discursos FOMC (2018–2025)")
plt.tight_layout()
plt.show()
