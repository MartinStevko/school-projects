s = input()
p = ''
while s != '0':
    if s == s[::-1]:
        if p:
            print(p, end=' ')
        p = s
    s = input()

print(p)
