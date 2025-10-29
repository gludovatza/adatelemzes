import numpy as np
import matplotlib.pyplot as plt

n = 10_000  # az aláhúzás csak a jobb olvashatóság kedvéért van
kocka = np.random.randint(1, 7, size=n) # 1-től 6-ig terjedő véletlen egész számok generálása n-szer

# Gyakoriságok számítása
egyedi, db = np.unique(kocka, return_counts=True) # egyedi értékek és azok gyakoriságai
gyakorisag_szazalek = db / n * 100

# Kiírás
for szam, gyak in zip(egyedi, gyakorisag_szazalek): # párhuzamos iteráció
    print(f"{szam}: {gyak:.2f}%")

# Vizualizáció
plt.bar(egyedi, gyakorisag_szazalek, color="cornflowerblue")
plt.title("Dobókocka dobások eloszlása (10 000 kísérlet)")
plt.xlabel("Dobott szám")
plt.ylabel("Gyakoriság (%)")
plt.grid(axis="y", linestyle="--", alpha=0.7) # vízszintes rácsvonalak a jobb olvashatóságért
plt.show()
