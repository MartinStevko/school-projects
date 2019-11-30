from copy import deepcopy


# vrati suradnice n-teho najblizsieho volneho policka
def get_free(arr):
    for i in range(width):
        for j in range(height):
            if arr[i][j]:
                return i, j

    return None


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


# hlavna funkcia, ktora rekurzivne prejde vsetky perspektivne pozicie
def independency(x, y, posits, arr):
    global output
    # tato podmienka zrychluje algoritmus na zaklade matematickeho
    # invariantu, ak by sme ju nepouzili, algoritmus najde vsetky
    # moznosti ako mozu byt figurky rozmiestnene, ale trva dlhsie
    if len(output[0]) < max_c:
        posits.append((x, y))
        arr = endanger(x, y, arr)

        pos = get_free(arr)
        while pos is not None:
            independency(pos[0], pos[1], posits[:], deepcopy(arr))
            arr[pos[0]][pos[1]] = False
            pos = get_free(arr)

        if len(posits) > len(output[0]):
            output = [posits]
        elif len(posits) == len(output[0]):
            output.append(posits)


# spustac hlavnej funkcie
def independent():
    # 2D pole na znacenie odskusanych moznosti
    b = [True]*height
    blank = []
    for i in range(width):
        blank.append(b[:])

    pos = get_free(blank)
    while pos is not None:
        independency(pos[0], pos[1], [], deepcopy(blank))
        blank[pos[0]][pos[1]] = False
        pos = get_free(blank)


# volba figurky (kral/dama/strelec/kon/veza) a rozmerov
chessman = 'kon'
width = 5
height = 5

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
# maximum figurok (nie nutne dosiahnutelne)
if chessman == 'kral':
    moves, vector, max_c = ch_set[0], False, (width*height+3)//4
if chessman == 'dama':
    moves, vector, max_c = ch_set[1], True, min(width, height)
if chessman == 'strelec':
    moves, vector, max_c = ch_set[2], True, min(width, height)
if chessman == 'kon':
    moves, vector, max_c = ch_set[3], False, (width*height+1)//2
if chessman == 'veza':
    moves, vector, max_c = ch_set[4], True, min(width, height)

# najvyssi najdeny pocet polozenych figurok a moznosti ich suradnic
output = [[]]

# vypis vysledkov
independent()
print('Max. pocet: '+str(len(output[0])))
print('Napr.: '+str(output[0]))
