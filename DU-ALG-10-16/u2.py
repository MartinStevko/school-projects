# Martin Stevko


def sucin(x, y):
    v = [0]*(len(x)+len(y))
    x += [0]
    o = 0
    for j in range(len(y)):
        for i in range(len(x)):
            t = (v[i+j] + o + x[i]*y[j])
            v[i+j] = t % 10
            o = t//10

    v = v[::-1]
    if v[0] == 0:
        return v[1:]
    else:
        return v


a = [int(x) for x in input('Prve cislo:\n>')[::-1]]
b = [int(x) for x in input('Druhe cislo:\n>')[::-1]]

if len(a) >= len(b):
    s = sucin(a, b)
else:
    s = sucin(b, a)

print(*s, sep='')
