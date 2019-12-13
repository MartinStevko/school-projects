import id_api


class AllocatorId:

    def __init__(self, n):
        self.free = id_api.IAllocatorId(1, n)
        self.allocated = None

    def get(self):
        if self.free is not None:
            f = self.free
            f.allocated = True
            self.free = f.next
            f.next.prev = None
        else:
            raise Exception('No ID is free right now.')

        if self.allocated is not None:
            f.next = self.allocated
            self.allocated.prev = f
            self.allocated = f
        else:
            f.next = None
            self.allocated = f

        return f.N

    def back(self, id):
        ##### Dostanie ID namiesto cisla #####
        n = self.allocated
        while n is not None and n.N != id:
            n = n.next
        else:
            if n is None:
                raise Exception('This ID is free and can not be returned back.')
            else:
                id = n
        ######################################

        if not id.allocated:
            raise Exception('This ID is free and can not be returned back.')

        id.allocated = False
        if id.next is None and id.prev is None:
            self.allocated = None
        elif id.next is None:
            id.prev.next = None
            id.prev = None
        elif id.prev is None:
            id.next.prev = None
            self.allocated = id.next
        else:
            id.next.prev = id.prev
            id.prev.next = id.next
            id.prev = None

        if self.free is not None:
            id.next = self.free
            self.free.prev = id
        else:
            id.next = None

        self.free = id

    def get_alives(self):
        out = []
        n = self.allocated
        while n is not None:
            out.append(n.N)
            n = n.next

        return out

    def get_deads(self):
        out = []
        n = self.free
        while n is not None:
            out.append(n.N)
            n = n.next

        return out
