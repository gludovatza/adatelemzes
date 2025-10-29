import csv
import statistics
import matplotlib.pyplot as plt # pip install matplotlib

# Új beolvasás az időjárás oszloppal
napok = []
homersekletek = []
idojarasok = []

with open("homerseklet2.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for sor in reader:
        napok.append(int(sor["nap"]))
        homersekletek.append(float(sor["hőmérséklet"]))
        idojarasok.append(sor["időjárás"])

# Kategóriák számlálása
statisztika = {}

for allapot in idojarasok:
    statisztika[allapot] = statisztika.get(allapot, 0) + 1

# Kiírás
print("Időjárás statisztika:")
for tipus, db in statisztika.items():
    print(f"- {tipus.capitalize()}: {db} nap")

szinek = {
    "napos": "gold", 
    "felhős": "gray", 
    "esős": "skyblue"
    }
szinlista = [szinek[i] for i in idojarasok]

plt.scatter(napok, homersekletek, c=szinlista, s=60)
plt.title("Napi hőmérsékletek és időjárás típusa")
plt.xlabel("Nap")
plt.ylabel("Hőmérséklet (°C)")
plt.grid(True)
plt.show()
