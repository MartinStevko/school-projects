def prevod(z, co, na):
    if z == 10:
        n = int(co)
    else:
        n = 0
        lc = len(co)
        for i in range(lc):
            n *= z
            n += int(co[i])

    if na == 10:
        return n
    else:
        v = ''
        while n >= na:
            v += str(n % na)
            n //= na

        v += str(n)

        return v[::-1]


za, a, zb, b, zv = input().split()
za, zb, zv = int(za), int(zb), int(zv)

a = prevod(za, a, 10)
b = prevod(zb, b, 10)

print(prevod(10, a+b, zv))
print(prevod(10, a-b, zv))
print(prevod(10, a*b, zv))
print(prevod(10, a//b, zv))
