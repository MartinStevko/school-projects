import json
import random

# Vyber typu skusania
dictionary = input("Type (general/ips/pcs): ")
while dictionary not in ["general", "ips", "pcs"]:
    print("Wrong input!")
    dictionary = input("Type (general/ips/pcs): ")

# Nacitanie dat
with open(dictionary+".json", encoding="utf-8") as f:
    d = json.load(f)

# Nacitanie pocetnosti zodpovedani
with open(dictionary+"_data.json", encoding="utf-8") as f:
    q = json.load(f)

# Hlavny cyklus
s = 0
n = 0
while True:
    # Najdenie slova
    key = random.choice(list(d.keys()))
    q_min = q[min(q, key=lambda i: q[i])]
    if key not in q.keys():
        q[key] = 0
    if q[key] > q_min+1:
        acc = []
        for k in q.keys():
            if q[k] == q_min:
                acc.append(k)
        key = random.choice(acc)

    # Vypis otazky
    print(*d[key]["sk"], sep=", ", end=' - ')

    # Kontrola odpovede
    if input() not in d[key]["en"]:
        print(f"Nie! Je to {key}.")
        n += 1
    else:
        q[key] += 1
        s += 1

    # Vypis skore
    if (s+n) % 10 == 0:
        # Zapis pocetnosti odpovedi
        with open(dictionary+"_data.json", "w", encoding="utf-8") as f:
            json.dump(q, f, indent=4, ensure_ascii=False)

        print(f"Správne: {s}\nNesprávne: {n}\n\nPre pokračovanie stlač Enter, ináč napíš 'exit'.")
        if input() == "exit":
            print("Good bye!")
            break
