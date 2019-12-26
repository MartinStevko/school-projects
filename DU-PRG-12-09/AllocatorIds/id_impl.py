import id_api


class AllocatorId:

    def __init__(self, n):
        self.array = []
        self.array.append(
            id_api.IAllocatorId(n=1)
        )
        for i in range(1, n-1):
            self.array.append(
                id_api.IAllocatorId(p=i-1, n=i+1)
            )
        self.array.append(
            id_api.IAllocatorId(p=n-1)
        )

        self.free = 0
        self.allc = None

    def get(self):
        if self.free is not None and self.array[self.free].next is not None:
            i = self.free
            self.array[i].allocated = True
            self.free = self.array[i].next
            self.array[self.array[i].next].prev = None
        elif self.free is not None:
            i = self.free
            self.array[i].allocated = True
            self.free = self.array[i].next
        else:
            raise Exception('No ID is free right now.')

        if self.allc is not None:
            self.array[i].next = self.allc
            self.array[self.allc].prev = i
            self.allc = i
        else:
            self.array[i].next = None
            self.allc = i

        return i

    def back(self, id):
        if not self.array[id].allocated:
            raise Exception('This ID is free and can not be returned back.')

        self.array[id].allocated = False
        if self.array[id].next is None and self.array[id].prev is None:
            self.allc = None
        elif self.array[id].next is None:
            self.array[self.array[id].prev].next = None
            self.array[id].prev = None
        elif self.array[id].prev is None:
            self.array[self.array[id].next].prev = None
            self.allc = self.array[id].next
        else:
            self.array[self.array[id].next].prev = self.array[id].prev
            self.array[self.array[id].prev].next = self.array[id].next
            self.array[id].prev = None

        if self.free is not None:
            self.array[id].next = self.free
            self.array[self.free].prev = id
        else:
            self.array[id].next = None

        self.free = id

    def get_alives(self):
        out = []
        i = self.allc
        while i is not None:
            out.append(i)
            i = self.array[i].next

        return out

    def get_deads(self):
        out = []
        i = self.free
        while i is not None:
            out.append(i)
            i = self.array[i].next

        return out
