
from data import l02 as l

print('Beží spúšťač úloh riešených ako DÚ z L02 Programovanie 1. Pre\
ukončenie zadajte prázdny vstup, pri výzve na zadanie čísla úlohy.')

s = input('Zadajte číslo úlohy, ktorej riešenie sa má spustiť: ')
while s:
    try:
        s = int(s)
    except(ValueError):
        print('Nesprávny vstup.')
    else:
        if s < 10:
            f = f'e0{str(s)}'
        else:
            f = f'e{str(s)}'

        getattr(l, f)()

    s = input('Zadajte číslo úlohy, ktorej riešenie sa má spustiť: ')
