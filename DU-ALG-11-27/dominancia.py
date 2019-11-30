from copy import deepcopy


# vsetky ohrozene alebo obsade policka nastavi tak, ze uz nie su volne
def endanger(x, y, arr):
    if vector:
        for m in moves:
            k = 0
            while True:
                i, j = (x + k*m[0]) % width, (y + k*m[1]) % height
                arr[i][j] = False
                if i == x and j == y and k != 0:
                    break

                k += 1
    else:
        arr[x][y] = False
        for m in moves:
            i, j = (x + m[0]) % width, (y + m[1]) % height
            arr[i][j] = False

    return arr


# funkcia, ktora z poradoveho cisla policka vrati jeho index v poli
def resolve(n):
    x = n % width
    y = n // width
    return x, y


# hlavna funkcia, ktora rekurzivne prejde vsetky pozicie
def dominance(n, posits, arr):
    global output
    # tato podmienka zrychluje algoritmus na zaklade matematickeho
    # invariantu, ak by sme ju nepouzili, algoritmus najde vsetky
    # moznosti ako mozu byt figurky rozmiestnene, ale trva dlhsie
    if len(output[0]) > min_c:
        posits.append(resolve(n))
        t = resolve(n)
        endanger(t[0], t[1], arr)
        if dominant(arr):
            if len(posits) < len(output[0]):
                output = [posits]
            elif len(posits) == len(output[0]):
                output.append(posits)
            posits = []
        else:
            for k in range(n+1, width*height):
                dominance(k, posits[:], deepcopy(arr))


# zisti ci je rozlozenie dominantne
def dominant(arr):
    for row in arr:
        if True in row:
            return False
    return True


# volba figurky (kral/dama/strelec/kon/veza) a rozmerov
chessman = 'dama'
width = 5
height = 5

# vyuzitie symetrickosti pre urychlenie vypoctu
if width > height:
    width, height = height, width

# mnozina tahov jednotlivych figurok popisana vektorom
ch_set = [
    # kráľ
    [(1, 0), (1, -1), (0, 1), (1, 1), (-1, 0), (-1, 1), (0, -1), (-1, -1)],
    # dáma
    [(1, 0), (1, -1), (0, 1), (1, 1)],
    # strelec
    [(1, -1), (1, 1)],
    # kôň
    [(2, -1), (1, -2), (1, 2), (2, 1), (-2, 1), (-1, 2), (-1, -2), (-2, -1)],
    # veža
    [(1, 0), (0, 1)],
]

# popis policok kam sa z aktualneho viem zvolenou figurkou dostat a 
# minimum figurok (nie nutne dosiahnutelne)
if chessman == 'kral':
    moves, vector, min_c = ch_set[0], False, (width*height+8)//9
if chessman == 'dama':
    moves, vector, min_c = ch_set[1], True, 1
if chessman == 'strelec':
    moves, vector, min_c = ch_set[2], True, 1
if chessman == 'kon':
    moves, vector, min_c = ch_set[3], False, (width*height+8)//9
if chessman == 'veza':
    moves, vector, min_c = ch_set[4], True, min(width, height)

# najnizsi najdeny pocet polozenych figurok a moznosti ich suradnic
output = [[None]*width*height]

# vypis vysledkov
b = [True]*height
blank = []
for i in range(width):
    blank.append(b[:])
dominance(0, [], blank)
print('Min. pocet: '+str(len(output[0])))
print('Napr.: '+str(output[0]))
