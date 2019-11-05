import sys

s = 0
m = False
z = ord(sys.stdin.read(1))
while z != 10:
    c = 0
    while (z < 48 or z > 57):
        if z == 45:
            m = not m

        z = ord(sys.stdin.read(1))
        continue

    while z >= 48 and z <= 57:
        c = 10*c+z-48
        z = ord(sys.stdin.read(1))

    if m:
        if c == 1:
            break
        else:
            s -= c
            m = False
    else:
        s += c

print(s)
