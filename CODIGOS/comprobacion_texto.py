import pandas as pd
df = pd.read_csv("/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv")
df["longitud"] = df["texto_limpio"].astype(str).apply(lambda x: len(x.split()))
print(df.sort_values("longitud", ascending=False).head(58))
