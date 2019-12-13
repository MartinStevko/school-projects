class Car:

    def __init__(self, length, weight):
        self.length = length
        self.weight = weight

        self.next = None


class Train:

    def __init__(self):
        self.first = None
        self.last = None

        self.length = 0
        self.weight = 0

    def add(self, length, weight):
        self.length += length
        self.weight += weight

        if self.last is not None:
            self.last.next = Car(length, weight)
            self.last = self.last.next
        else:
            self.last = Car(length, weight)
            self.first = self.last

    def remove(self):
        self.length -= self.first.length
        self.weight -= self.first.weight

        self.first = self.first.next


def get_num(f):
    ch = f.read(1)
    if ch == '':
        return None
    else:
        o = ord(ch)

    while o < 48 or o > 58:
        if o == 45:
            return None
        ch = f.read(1)
        if ch == '':
            return None
        else:
            o = ord(ch)

    num = 0
    while 48 <= o and o <= 58:
        num = 10*num + o - 48
        ch = f.read(1)
        if ch == '':
            break
        else:
            o = ord(ch)

    return num


for i in range(1, 15):
    with open('Train_and_bridge/'+str(i)+'.in', 'r') as f:
        t = Train()
        bridge_length = get_num(f)
        bridge_capacity = get_num(f)

        overload = -1
        i = 0
        length = get_num(f)
        weight = get_num(f)
        while length is not None and weight is not None:
            t.add(length, weight)
            i += 1

            while t.length - t.first.length - t.last.length >= bridge_length:
                t.remove()
            if t.weight > bridge_capacity:
                overload = i
                break
            else:
                length = get_num(f)
                weight = get_num(f)

        print(overload)
