import pandas as pd
import matplotlib.pyplot as plt

# cargar datos
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_mensual.csv')
df_sp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/HistoricalData_S&P500.csv')

# datos del sp500
df_sp["Fecha"] = pd.to_datetime(df_sp["Fecha"], dayfirst=True)
df_sp = df_sp.rename(columns={"Cerrar/último": "cierre"})

df_sp["cierre"] = pd.to_numeric(df_sp["cierre"], errors='coerce')

# sentimiento
df_sent["fecha"] = pd.to_datetime(df_sent["fecha"])
df = pd.merge(df_sent, df_sp, left_on="fecha", right_on="Fecha", how="inner")

# detectar outliers por sentimiento 
q10 = df["sentimiento_textblob"].quantile(0.10)
q90 = df["sentimiento_textblob"].quantile(0.90)
outliers = df[(df["sentimiento_textblob"] <= q10) | (df["sentimiento_textblob"] >= q90)]

# resultados
print(" Discursos con sentimiento extremo (outliers):")
print(outliers[["fecha", "sentimiento_textblob", "cierre"]].sort_values("fecha"))

# guardar resultados
outliers[["fecha", "sentimiento_textblob", "cierre"]].sort_values("fecha").to_csv(
    "/Users/carcerezo/Desktop/TFG/outliers_eventos.csv", index=False
)

# visualización
plt.figure(figsize=(10, 6))
plt.scatter(df["sentimiento_textblob"], df["cierre"], alpha=0.5, label="Todos los discursos")
plt.scatter(outliers["sentimiento_textblob"], outliers["cierre"], color="red", label="Outliers")
plt.xlabel("Sentimiento TextBlob")
plt.ylabel("S&P 500 (cierre)")
plt.title("Outliers: Sentimiento extremo vs. cierre del S&P 500")
plt.legend()
plt.tight_layout()
plt.savefig("/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales/outliers_sp500.png")
plt.close()
