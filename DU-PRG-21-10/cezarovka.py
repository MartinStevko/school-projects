p = int(input())
s = ''
for z in input():
    if z == ' ':
        s += ' '
    else:
        s += chr((ord(z)-71+p) % 26 + 97)

print(s)
