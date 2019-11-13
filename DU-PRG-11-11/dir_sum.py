from os import stat, listdir
from os.path import isfile, isdir

path = input('Path: ')
if not path:
    path = '.'

def get_size(d='.'):
    s = 0
    for obj in listdir(d):
        p = d + '/' + obj
        if isdir(p):
            s += get_size(p)
        elif isfile(p):
            s += stat(p).st_size
        else:
            raise OSError(obj+' is not file nor directory.')

    return s

size = get_size(path)

key = 'B'
prefixes = ['', 'k', 'M', 'G', 'T']

s = ''
i = 0
while size > 0 and i<4:
    key = prefixes[i]+'B'
    s = f'{size%1000} {key} {s}'

    size //= 1000
    i += 1

print(s)
