# szogyak_numpy.py
import numpy as np

# --- 0) Betöltés (TSV) -> strukturált NumPy tömb -----------------------------
def load_szo10000(path="szo10000.txt"):
    # A fájl első sora tartalmazza a fejlécet (azon, szoto, szofaj, gyakori)
    # Tabulátor a határoló, UTF-8 kódolás
    tbl = np.genfromtxt(
        path,
        delimiter="\t",
        names=True,          # fejléc -> oszlopnevek
        dtype=None,          # típusok automatikus felismerése
        encoding="utf-8"
    )
    # Biztonság kedvéért kényszerítjük a típusokat: https://www.w3schools.com/python/numpy/numpy_data_types.asp
    tbl = tbl.astype([("azon", np.int64), ("szoto", "U100"), ("szofaj", "U3"), ("gyakori", np.int64)])
    return tbl

# Segéd függvények
def select(table, cols):
    return table[cols].copy()

def order_by(table, key, ascending=True):
    idx = np.argsort(table[key])
    return table[idx] if ascending else table[idx[::-1]] # -1 itt a léptetés nagysága

def limit(table, n=10):
    return table[:n] # start: elejétől, stop: n-edik elemig

def print_table(arr, title=None):
    if title:
        print(f"\n=== {title} ===")
    print(arr)

# --- 1) Fő program ------------------------------------------------------------
if __name__ == "__main__":
    szavak = load_szo10000("szo10000.txt")

    # 2) 2ige500 – Azok az igék (szofaj == 'ige'), amelyek gyakori >= 500000 -> csak szótő(k)
    mask_2 = (szavak["szofaj"] == "ige") & (szavak["gyakori"] >= 500_000) # SQL WHERE utáni szűrési feltétel a maszkolás
    q2 = szavak["szoto"][mask_2]  # csak a szótövek, egyedileg
    print("2. feladat")
    for s in q2:
        print(s)

    # 3) 3brmellek – Melléknevek (mn), amelyek szótöve 'br'-rel kezdődik; jelenjen meg a szótő és a gyakoriság
    mask_3 = (szavak["szofaj"] == "mn") & (np.char.startswith(szavak["szoto"], "br"))
    q3 = select(szavak[mask_3], ["szoto", "gyakori"])
    # opcionális: rendezzük gyakoriság szerint csökkenőbe, hogy áttekinthetőbb legyen
    q3 = order_by(q3, "gyakori", ascending=False)
    print_table(q3, "(3) 3brmellek - 'br*' kezdetű melléknevek (szoto, gyakori)")

    # 4) 4hatar10 – 10 leggyakoribb határozószó (hsz)
    mask_4 = (szavak["szofaj"] == "hsz")
    q4 = select(szavak[mask_4], ["szoto", "gyakori"])
    q4 = order_by(q4, "gyakori", ascending=False)
    q4 = limit(q4, 3)
    print_table(q4, "(4) 4hatar10 - Top 10 határozószó (szoto, gyakori)")

    # # 5) 5szofajok – Szófajonként hány szótő szerepel (count szoto csoportonként)
    # # Itt a feladat a rekordok számát kéri szófajonként; a TSV minden sor egy (szoto, szofaj) előfordulás,
    # # tehát elég a csoportonkénti darabszám.
    # szofajok, counts = np.unique(szavak["szofaj"], return_counts=True)
    # q5_dtype = [("szofaj", "U10"), ("db", np.int64)]
    # q5 = np.zeros(szofajok.shape[0], dtype=q5_dtype)
    # q5["szofaj"] = szofajok
    # q5["db"] = counts
    # # opcionális: rendezzük csökkenő db szerint
    # q5 = order_by(q5, "db", ascending=False)
    # print_table(q5, "(5) 5szofajok - Szófajonkénti szótő darabszám (szofaj, db)")

    # # 6) 6tobb – Azok a szótövek, amelyek legalább háromszor szerepelnek az adatbázisban
    # # (több szófajban is előfordulhat ugyanaz a szótő)
    # uniq_szoto, szamlalo = np.unique(szavak["szoto"], return_counts=True)
    # mask_6 = (szamlalo >= 3)
    # q6 = np.sort(uniq_szoto[mask_6])  # ábécérendben
    # print("\n=== (6) 6tobb - Legalább 3-szor előforduló szótövek ===")
    # for s in q6:
    #     print(s)

    # --- Extra: ha szeretnéd fájlba is menteni az eredményeket ----------------
    # np.savetxt("q3_brmellek.csv", q3, fmt="%s,%d", header="szoto,gyakori", comments="", encoding="utf-8")
    # np.savetxt("q4_hatar10.csv", q4, fmt="%s,%d", header="szoto,gyakori", comments="", encoding="utf-8")
    # np.savetxt("q5_szofajok.csv", q5, fmt="%s,%d", header="szofaj,db", comments="", encoding="utf-8")
    # np.savetxt("q2_ige500.txt", q2, fmt="%s", encoding="utf-8")
    # np.savetxt("q6_legalabb3.txt", q6, fmt="%s", encoding="utf-8")
