import pandas as pd

# Cargar el CSV
ruta = "/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv"
df = pd.read_csv(ruta)

# columna de longitud
df["longitud"] = df["texto_limpio"].apply(len)

# 10 mas largos
print("\n Top 10 discursos más largos:")
print(df[["año", "archivo", "longitud"]].sort_values(by="longitud", ascending=False).head(10))

# metricas generales
print("\n Métricas generales:")
print("Longitud mínima:", df["longitud"].min())
print("Longitud máxima:", df["longitud"].max())
print("Longitud media:", round(df["longitud"].mean(), 2))

# texto más largo
print("\n Fragmento del discurso más largo:")
ejemplo = df.loc[df["longitud"].idxmax(), "texto_limpio"]
print(ejemplo[:2000])  # primeros 2000 caracteres
