import sys


def pridaj_z(z):
    if z in '+-':
        vp = '+-*/)'
    elif z in '*/':
        vp = '*/)'
    else:
        vp = ')'

    while len(znamienka) > 0 and znamienka[-1] in vp:
        if len(cisla) == 1:
            break
        else:
            vyhodnot(znamienka.pop())
    else:
        znamienka.append(z)


def vyhodnot_z():
    temp = []
    z = znamienka.pop()
    while z != '(':
        vyhodnot(z)
        z = znamienka.pop()


def vyhodnot(z):
    if z == '+':
        r = cisla.pop()
        l = cisla.pop()
        cisla.append(l+r)
    elif z == '-':
        r = cisla.pop()
        l = cisla.pop()
        cisla.append(l-r)
    elif z == '*':
        r = cisla.pop()
        l = cisla.pop()
        cisla.append(l*r)
    elif z == '/':
        r = cisla.pop()
        l = cisla.pop()
        cisla.append(l//r)
    elif z == ')':
        vyhodnot_z()
    else:
        raise ValueError('Nespravne uzatvorkovanie')


while True:
    print('Novy vyraz')
    # Zasobniky
    cisla = []
    znamienka = []

    # Nacitanie vstupu
    temp = None
    z = sys.stdin.read(1)
    while z != '=':
        if z in '+-*/()':
            if temp is not None:
                cisla.append(temp)
                temp = None

            pridaj_z(z)

        elif 47 < ord(z) and ord(z) < 58:
            if temp is not None:
                temp = 10*temp + ord(z) - 48
            else:
                temp = ord(z) - 48

        else:
            if temp is not None:
                cisla.append(temp)
                temp = None

        z = sys.stdin.read(1)

    if temp is not None:
        cisla.append(temp)
        temp = None

    # Vyhodnotenie
    while len(znamienka) > 0:
        z = znamienka.pop()
        vyhodnot(z)

    if len(cisla) == 1:
        print(cisla[0])
    else:
        raise ValueError('Nespravne zadany vyraz')
