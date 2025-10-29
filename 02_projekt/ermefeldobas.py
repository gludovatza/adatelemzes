import numpy as np
import matplotlib.pyplot as plt

# Érmefeldobás szimuláció
n = 10_000
erme = np.random.randint(0, 2, size=n)  # 0 vagy 1 értékek

# Statisztika
fej_db = np.sum(erme == 1)
iras_db = np.sum(erme == 0)
fej_arany = fej_db / n * 100
iras_arany = iras_db / n * 100

print(f"Összes dobás: {n}")
print(f"Fej: {fej_db}, Írás: {iras_db}")
print(f"A fejek aránya: {fej_arany:.2f}%")
print(f"Az írások aránya: {iras_arany:.2f}%")

# Vizualizáció
plt.bar(('fej', 'írás'), (fej_arany, iras_arany))
plt.title("Dobások eloszlása (10 000 kísérlet)")
plt.xlabel("Dobott szám")
plt.ylabel("Gyakoriság (%)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()