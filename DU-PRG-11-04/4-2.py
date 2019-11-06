p = input('Relative path:')

frekvencia = {}
with open(p, 'r', encoding='utf-8') as f:
    for s in f.read().split():
        if s in frekvencia.keys():
            frekvencia[s] += 1
        else:
            frekvencia[s] = 1

order = sorted(frekvencia.keys(), key = lambda k: -frekvencia[k])

s = sum(frekvencia.values())
print('Sum:')
print(s)

print('Most frequent:')
k = 0
m = frekvencia[order[k]]
while k<len(order) and frekvencia[order[k]] == m:
    print(order[k])
    k += 1

print('Average:')
print(s/len(frekvencia.items()))

print('Median frequent:')
med = frekvencia[order[(len(order)-1)//2]]
for k in order:
    if frekvencia[k] == med:
        print(k)

print('Least frequent:')
k = len(order)-1
l = frekvencia[order[k]]
while k>=0 and frekvencia[order[k]] == l:
    print(order[k])
    k -= 1
