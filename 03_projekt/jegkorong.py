import numpy as np

# --- 0) Betöltés (TSV) -> strukturált NumPy tömb -----------------------------

# segédfüggvény a konvertáláshoz
def to_iso_date(s):
    return s.replace('.', '-')

def load_hoki(path="hoki.txt"):
    # A fájl első sora tartalmazza a fejlécet (azon, szoto, szofaj, gyakori)
    # Tabulátor a határoló, UTF-8 kódolás
    tbl = np.genfromtxt(
        path,
        delimiter="\t",
        names=True,          # fejléc -> oszlopnevek
        dtype=None,          # típusok automatikus felismerése
        converters={0: to_iso_date},  # 0-s indexű oszlop: datum konvertálása!
        encoding=None
        
    )
    # Biztonság kedvéért kényszerítjük a típusokat: https://www.w3schools.com/python/numpy/numpy_data_types.asp
    # a datetime-ot már előtte konvertáltam, így csak 'D' pontosságú dátum lesz
    tbl = tbl.astype([("datum", 'datetime64[D]'), ("ellenfel", "U100"), ("lott", np.int64), ("kapott", np.int64), ("tipus", "U100"), ("helyszin", "U100"), ("mpont", np.int64), ("epont", np.int64), ("mhelyezes", np.int64), ("ehelyezes", np.int64)])
    
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
    meccsadatok = load_hoki("hoki.txt")
    

    # 2) 
    mask_2 = (meccsadatok["ellenfel"] == "Canada")  
    q2 = select(meccsadatok[mask_2], ["datum", "lott", "kapott"])  
    print("2. feladat")
    for s in q2:
        print(s)

    # 3,
    print("3. feladat:")
    q3 = select(meccsadatok, ["lott", "kapott"])
    
    # legtöbb lőtt gól:
    q3_max_lott = order_by(q3, "lott", ascending=False)
    q3_max_lott =limit(q3_max_lott,1)
    print(q3_max_lott["lott"])
    
    # legtöbb kapott gól:
    q3_max_kapott = order_by(q3, "kapott", ascending=False)
    q3_max_kapott =limit(q3_max_kapott,1)
    print(q3_max_kapott["kapott"])
    
    # VAGY még sokkal egyszerűbben:
    print("Legtöbb lőtt gól:", np.max(meccsadatok["lott"]))
    print("Legtöbb kapott gól:", np.max(meccsadatok["kapott"]))
    
    # 4) 
    print("4. feladat:")
    unique_cats, inverse_idx = np.unique(meccsadatok["ellenfel"], return_inverse=True)
    counts = np.array([(inverse_idx == i).sum() for i in range(len(unique_cats))])
    mask_4 = counts == 1
    print(unique_cats[mask_4])
    
    # ellenőrzés
    for cat, count in zip(unique_cats, counts):
        # if(count == 1): # ha nem a teljes listát akarjuk kiírni
            print(f"{cat}: {count}")
    # 5)
    print("5. feladat:")
    mask_5 = (meccsadatok["datum"] >= np.datetime64("1945-05-08"))  & (meccsadatok["tipus"] != "") # datetime64-gyé alakítottam a szöveget
    q5 = select(meccsadatok[mask_5], ["datum"])  
    q5 = order_by(q5, "datum", ascending=True) # növekvőbe kell!
    q5 = limit(q5,1)
    print(q5)
    
    #6)
    print("6. feladat:")
    mask_6 = (meccsadatok["ehelyezes"] == 1) # az 1 nem szöveges
    q6 = select(meccsadatok[mask_6], ["ellenfel"])  #distinct? --> igen, lásd a következő sort!
    q6 = np.unique(q6["ellenfel"])
    print(q6)

    #7)
    print("7. feladat:")
    mask_7 = (meccsadatok["helyszin"] != "Hungary")  & (meccsadatok["helyszin"] != meccsadatok["ellenfel"]) # Hungary nagy kezdőbetűs
    q7 = select(meccsadatok[mask_7], ["datum"])  #count*? --> igen, úgyhogy itt lekérhetjük bármelyik oszlopot, aztán megszámoljuk az eredményhalmazt
    print(len(q7))

    #8
    # Márk kódja:
    # mask_8 = (meccsadatok["datum"] == "1929.01.24")
    # q8 = select(meccsadatok[mask_8], ["datum"])  #count?
    # print(q8)
    
    print("8. feladat:")
    # lekérjük a legkisebb dátumot, amikor a lőtt gólok száma nagyobb volt, mint a kapott gólok száma, tehát amikor először nyertünk
    mask_8 = (meccsadatok["lott"] > meccsadatok["kapott"])
    q8 = select(meccsadatok[mask_8], ["datum"])
    
    # v1: Így is lehetne: order by + limit
    # elso_nyertes_meccs = order_by(q8, "datum", ascending=True)
    # elso_nyertes_meccs = limit(elso_nyertes_meccs,1)
    # print(elso_nyertes_meccs)
    
    # v2: egyszerűbben: min függvénnyel
    elso_nyertes_meccs = q8["datum"].min()
    print("Először nyertünk:", elso_nyertes_meccs)
    
    # felhasználjuk a segédszámítást (elso_nyertes_meccs) és megszámoljuk, hány meccs volt előtte (hány vereség vagy döntetlen)
    mask_8b = meccsadatok["datum"] < elso_nyertes_meccs
    q8b = select(meccsadatok[mask_8b], ["datum"])
    print("Első győzelem előtt ennyi meccs volt:", len(q8b))
    