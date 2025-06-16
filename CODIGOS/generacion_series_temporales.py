import pandas as pd

# ruta
ruta = '/Users/carcerezo/Desktop/TFG/discursos_con_sentimiento_textblob.csv'
df = pd.read_csv(ruta)

# columna fecha es de tipo datetime
df["fecha"] = pd.to_datetime(df["fecha"])

# columnas de año y mes
df["año"] = df["fecha"].dt.year
df["mes"] = df["fecha"].dt.month
df["año_mes"] = df["fecha"].dt.to_period("M").astype(str)  # formato tipo "2021-06"


sentimiento_mensual = df[["fecha", "año", "mes", "año_mes", "sentimiento_textblob"]].copy()
sentimiento_mensual.sort_values(by="fecha", inplace=True)

# guardar  mensual
sentimiento_mensual.to_csv("/Users/carcerezo/Desktop/TFG/sentimiento_mensual.csv", index=False)



sentimiento_anual = df.groupby("año")["sentimiento_textblob"].mean().reset_index()
sentimiento_anual.rename(columns={"sentimiento_textblob": "sentimiento_medio_anual"}, inplace=True)

# guardar anual
sentimiento_anual.to_csv("/Users/carcerezo/Desktop/TFG/sentimiento_anual.csv", index=False)

print(" Archivos creados correctamente:")
print("- Sentimiento mensual → /TFG/sentimiento_mensual.csv")
print("- Sentimiento anual → /TFG/sentimiento_anual.csv")
