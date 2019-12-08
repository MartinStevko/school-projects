import json
import random
# import tkinter

dictionary = input("Type (general/ips/pcs): ")
while dictionary not in ["general", "ips", "pcs"]:
    print("Wrong input!")
    dictionary = input("Type (general/ips/pcs): ")

with open(dictionary+".json", encoding="utf-8") as f:
    d = json.load(f)

with open("data.json", encoding="utf-8") as f:
    q = json.load(f)

s = 0
n = 0
while True:
    key = random.choice(list(d.keys()))
    if q[key] > q[min(q, key=lambda i: q[i])]+1:
        key = min(q, key=lambda i: q[i])

    print(*d[key]["sk"], sep=", ", end=' - ')
    if input() not in d[key]["en"]:
        print(f"Nie! Je to {key}.")
        n += 1
    else:
        q[key] += 1
        s += 1
    if (s+n) % 10 == 0:
        print(f"Správne: {s}\nNesprávne: {n}\n\nPre pokračovanie stlač Enter, ináč napíš 'exit'.")
        if input() == "exit":
            print("Good bye!")
            break

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(q, f, indent=4, ensure_ascii=False)
