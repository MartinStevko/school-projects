# Vytvorenie dat
import random

n = int(input('n = '))
m = []
z = []
temp = [(x for x in range(n))]
navrhy = {}
for i in range(n):
    navrhy[i] = []
    m.append(random.shuffle(temp))
    z.append(random.shuffle(temp))

# Algoritmus stabilneho parovania
