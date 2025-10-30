import numpy as np
import matplotlib.pyplot as plt

# Adattartomány létrehozása 0 és 2π között, 1000 lépéssel
x = np.linspace(0, 2 * np.pi, 1000)

# A függvények kiszámítása
y_sin = np.sin(x)
y_cos = np.cos(x)

# A grafikon rajzolása
plt.figure(figsize=(10, 6))  # Nagyobb rajzterület
plt.plot(x, y_sin, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y_cos, label='cos(x)', color='red', linestyle='--', linewidth=2)

# Címek, jelmagyarázat, tengelyfeliratok
plt.title("Sin és cos függvény", fontsize=14)
plt.xlabel("x értékek (radián)", fontsize=12)
plt.ylabel("függvényérték", fontsize=12)
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ['0', 'π/2', 'π', '3π/2', '2π'])

plt.legend() # Jelmagyarázat megjelenítése
plt.grid(True, linestyle='dotted', alpha=0.7)

# A diagram elmentése (programozottan)
plt.savefig("sin_cos_plot.png", dpi=150)

# A diagram megjelenítése
plt.show()
