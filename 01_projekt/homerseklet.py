import csv
import statistics
import matplotlib.pyplot as plt # pip install matplotlib

# 1. Beolvasás
napok = []
homersekletek = []

with open("homerseklet.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for sor in reader:
        napok.append(int(sor["nap"]))
        homersekletek.append(float(sor["hőmérséklet"]))

# 2. Számítások
atlag = statistics.mean(homersekletek)
max_hom = max(homersekletek)
min_hom = min(homersekletek)
max_nap = napok[homersekletek.index(max_hom)]
min_nap = napok[homersekletek.index(min_hom)]
ingadozas = max_hom - min_hom

# 3. Eredmények kiírása
print(f"Havi átlaghőmérséklet: {atlag:.1f} °C")
print(f"Legmelegebb nap: {max_nap}. nap ({max_hom} °C)")
print(f"Leghidegebb nap: {min_nap}. nap ({min_hom} °C)")
print(f"Napi ingadozás: {ingadozas} °C")

# 4. Ábrázolás
# plt.plot(napok, homersekletek)
plt.plot(napok, homersekletek, marker='o', color='orange')
plt.title(f"Februári hőmérsékletek alakulása (Max és min: {max_hom} °C, {min_hom} °C)")
plt.xlabel("Nap")
plt.ylabel("Hőmérséklet (°C)")
plt.grid(True)
plt.show()

# Számítsd ki, hány nap volt átlag fölött!
atlag_feletti_napok = []
for h in homersekletek:
    if h > atlag:
        atlag_feletti_napok.append(h)
db = len(atlag_feletti_napok)

print(f"Átlag fölötti napok száma: {db} nap")

# Készíts egy függvényt, ami paraméterként kap egy listát, és visszaadja az átlagot (ne használd a statistics.mean-t).
def atlag_szamitas(lista):
    osszeg = sum(lista)
    db = len(lista)
    if db > 0:
        return osszeg / db
    else:
        return 0

# Használat
sajat_atlag = atlag_szamitas(homersekletek)
print(f"Saját függvénnyel számolt átlag: {sajat_atlag:.1f} °C")

# Írasd ki a 3 legmelegebb napot sorba rendezve!


# Bővítsd a fájlt új oszloppal: időjárás (pl. napos, felhős, esős), és készíts statisztikát, melyik típusból hány nap volt.