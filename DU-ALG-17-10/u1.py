# Vytvorenie dat
import random

n = int(input('n = '))
m = []
z = []
temp = []
odmietnutia = []
for i in range(n):
    temp.append(i)
    odmietnutia.append(True)
navrhy = {}
for i in range(n):
    navrhy[i] = []
    random.shuffle(temp)
    m.append(temp[:])
    random.shuffle(temp)
    z.append(temp[:])

# Algoritmus stabilneho parovania
while True in odmietnutia:
    # Podanie navrhov od muzov zenam
    for i in range(n):
        if odmietnutia[i]:
            navrhy[m[i][0]].append(i)
            del m[i][0]
            odmietnutia[i] = False

    # Vyhodnotenie navrhov
    for key in navrhy:
        mi = None
        # Ponechanie najlepsieho navrhu a odmietnutie zvysku
        for i in navrhy[key]:
            if mi is None:
                mi = i
                continue
            if (z[key].index(mi) > z[key].index(i)):
                odmietnutia[mi] = True
                mi = i
            else:
                odmietnutia[i] = True
        if mi:
            navrhy[key] = [mi]

# Vypis navrhov
print('(M, Z) = ', end='')
for k in navrhy:
    if k != n-1:
        print(f'({navrhy[k][0]}, {k})', end=', ')
    else:
        print(f'({navrhy[k][0]}, {k})')
