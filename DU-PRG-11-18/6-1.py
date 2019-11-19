class C:
    def __init__(self, real=0, img=0):
        self.real = real
        self.imaginary = img

    def __str__(self):
        if self.real and self.imaginary:
            if self.imaginary < 0:
                return f"{self.real} - {abs(self.imaginary)}i"
            else:
                return f"{self.real} + {self.imaginary}i"
        elif self.imaginary:
            return f"{self.imaginary}i"
        else:
            return str(self.real)

    def __add__(a, b):
        b = C.norm(b)
        return C(a.real + b.real, a.imaginary + b.imaginary)

    def __radd__(a, b):
        return a.__add__(b)

    def __sub__(a, b):
        b = C.norm(b)
        return C(a.real - b.real, a.imaginary - b.imaginary)

    def __rsub__(a, b):
        return a.__sub__(b)

    def __mul__(a, b):
        b = C.norm(b)
        r = a.real*b.real - a.imaginary*b.imaginary
        i = a.real*b.imaginary + a.imaginary*b.real

        return C(r, i)

    def __rmul__(a, b):
        return a.__mul__(b)

    def __gt__(a, b):
        b = C.norm(b)
        if a.real > b.real:
            return True
        elif a.real == b.real:
            if a.imaginary > b.imaginary:
                return True

        return False

    def __rgt__(a, b):
        return a.__lt__(b)

    def __lt__(a, b):
        b = C.norm(b)
        if a.real < b.real:
            return True
        elif a.real == b.real:
            if a.imaginary < b.imaginary:
                return True

        return False

    def __rlt__(a, b):
        return a.__gt__(b)

    def __neg__(self):
        return C().__sub__(self)

    def norm(self):
        if type(self) in [int, float]:
            return C(self)
        else:
            return self
