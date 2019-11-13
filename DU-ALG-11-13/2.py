class zoznam:

    def __init__(this, p=None):
        this.info = p
        this.pointer = this

    def __str__(this):
        s = ''
        c = this.pointer
        while c.info is not None:
            s += str(c.info)+', '
            c = c.pointer

        return s[:-2]

    def add(this, *new):
        for p in new:
            n = zoznam(p)
            n.pointer = this.pointer
            this.pointer = n

    def revert(this):
        c = this
        n = this.pointer
        while n.info is not None:
            # Posunutie na dalsi prvok
            l = c
            c = n
            n = c.pointer

            # Otocenie pointra
            c.pointer = l

        # Zmena pointra z prveho na posledny
        this.pointer = c


z = zoznam()
z.add(5, 4, 3, 2, 1, 0)
print(z)

z.revert()
print(z)
