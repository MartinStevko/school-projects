# Martin Stevko


class polynom:

    def __init__(this, *data, k=0, e=0):
        this.koeficient = k
        this.exponent = e
        this.pointer = this

        if data:
            this.add(*data)

    def __str__(this):
        s = ''
        c = this.pointer
        while c.koeficient != 0:
            k = abs(c.koeficient)
            if k == 1:
                temp = f'x^{c.exponent}'
            else:
                temp = f'{k}x^{c.exponent}'

            if c.koeficient > 0:
                s += ' + ' + temp
            elif c.koeficient < 0:
                s += ' - ' + temp

            c = c.pointer

        if s[1] == '+':
            return s[3:]
        else:
            return '-'+s[3:]

    def __add__(p, q):
        c = q.pointer
        while c.koeficient != 0:
            p.add((c.koeficient, c.exponent))
            c = c.pointer

        return p

    def add(this, *new):
        for elem in new:
            c = this
            while c.pointer.exponent > elem[1] and c.pointer.koeficient != 0:
                c = c.pointer

            if c.pointer.exponent == elem[1] and c.pointer.koeficient != 0:
                c.pointer.koeficient += elem[0]
                if c.pointer.koeficient == 0:
                    c.remove_next()

                n = c
            else:
                n = polynom(k=elem[0], e=elem[1])
                n.pointer = c.pointer
                c.pointer = n

            if this.exponent < n.exponent:
                this.exponent = n.exponent

    def remove_next(this):
        this.pointer = this.pointer.pointer

    def degree(this):
        return this.exponent


if __name__ == '__main__':
    p = polynom(
        (1, 2),
        (4, 5),
        (1, 2),
        (-1, 0),
        (-5, 7),
    )
    q = polynom(
        (2, 1),
        (-7, 2),
        (-4, 5),
        (5, 11),
    )

    print(f'({p}) + ({q}) = {p+q}')
