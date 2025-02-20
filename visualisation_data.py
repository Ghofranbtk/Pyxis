import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
file_path = "Subscriber volume by category-data-2025-02-18 17_01_49.csv"  # Remplace par le chemin de ton fichier

df = pd.read_csv(file_path)

# Filtrer les données pour contentType = FTP
df_ftp = df[df["contentType"] == "FTP"].copy()

# Convertir les timestamps en dates compréhensibles
df_ftp.loc[:, "ts"] = pd.to_datetime(df_ftp["ts"], unit='s')

# Trier les données par timestamp
df_ftp = df_ftp.sort_values(by="ts")

# Calculer la durée totale et le nombre d'heures consommées
start_time = df_ftp["ts"].min()
end_time = df_ftp["ts"].max()
total_hours = (end_time - start_time).total_seconds() / 3600

print(f"Période des données : de {start_time} à {end_time}")
print(f"Nombre total d'heures consommées : {total_hours:.2f} heures")

# Tracer et enregistrer la courbe complète
plt.figure(figsize=(10, 5))
plt.plot(df_ftp["ts"], df_ftp["value"], marker='o', linestyle='-', label="FTP Usage")
plt.xlabel("Timestamp")
plt.ylabel("Value")
plt.title("Visualisation des données FTP")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.savefig("ftp_usage_full.png")
plt.show()

# Filtrer les données pour les premières 24 heures
day_one = start_time + pd.Timedelta(hours=24)
df_24h = df_ftp[df_ftp["ts"] <= day_one]

plt.figure(figsize=(10, 5))
plt.plot(df_24h["ts"], df_24h["value"], marker='o', linestyle='-', label="FTP Usage - 1er Jour")
plt.xlabel("Timestamp")
plt.ylabel("Value")
plt.title("Visualisation des données FTP (1er Jour)")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.savefig("ftp_usage_1er_jour.png")
plt.show()

# Filtrer les données pour les premières 48 heures
day_two = start_time + pd.Timedelta(hours=48)
df_48h = df_ftp[df_ftp["ts"] <= day_two]

plt.figure(figsize=(10, 5))
plt.plot(df_48h["ts"], df_48h["value"], marker='o', linestyle='-', label="FTP Usage - 2 Premiers Jours")
plt.xlabel("Timestamp")
plt.ylabel("Value")
plt.title("Visualisation des données FTP (2 Premiers Jours)")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.savefig("ftp_usage_2_premiers_jours.png")
plt.show()
