n = int(input())
p = []
k = 2
while n % 2 == 0:
    n //= 2
    p.append(2)
k = 3
while k**2 <= n:
    if n % k == 0:
        n //= k
        p.append(k)
    else:
        if k % 6 == 1:
            k += 4
        else:
            k += 2

if n != 1:
    p.append(n)
print(*p)
