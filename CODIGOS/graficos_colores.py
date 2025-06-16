import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# CSV
df = pd.read_csv("/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv")

# longitud del texto
df["longitud_texto"] = df["texto_limpio"].apply(lambda x: len(str(x).split()))

# sacar año 
df["año"] = df["archivo"].apply(lambda x: re.search(r'20\d{2}', x).group(0) if re.search(r'20\d{2}', x) else None)

# Conteo de discursos por año
conteo_anual = df["año"].value_counts().sort_index()




plt.figure(figsize=(10, 5))
sns.barplot(x=conteo_anual.index, y=conteo_anual.values, palette="Set2")
plt.title("Discursos FOMC por año - Colores variados (Set2)")
plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


