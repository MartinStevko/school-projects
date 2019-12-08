a,b = [int(x) for x in input('a, b = ').split(',')]
m1 = '\\[\\begin{pmatrix}['+'c'*a+'|'+'c'*b+']\n'
m2 = '\\end{pmatrix}\\]'

s = input()
v = ''
while s != 'exit':
    if s == '':
        print(m1,v,m2, sep='')
        v = ''
    else:
        for i in s.split():
            v += f' {i} &'
        v = v[:-1]+'\\\\'+'\n'

    s = input()
