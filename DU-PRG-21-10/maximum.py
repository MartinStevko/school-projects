import sys

n = int(input())
m = 0
p = []
for i in range(n):
    z = ord(sys.stdin.read(1))
    c = 0
    while z >= 48 and z <= 57:
        c = 10*c+z-48
        z = ord(sys.stdin.read(1))

    if c > m:
        m = c
        p = [i+1]
    elif c == m:
        p.append(i+1)

print(m)
print(*p)
