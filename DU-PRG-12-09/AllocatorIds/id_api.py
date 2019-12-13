class IAllocatorId:
    N = 0
    allocated = False

    def __init__(self, n, m, prev=None):
        self.N = n
        self.prev = prev
        if m > n:
            self.next = IAllocatorId(n+1, m, self)
        else:
            self.next = None

    def get(self):
        NotImplemented

    def back(self, n):
        NotImplemented

    def get_alives(self):
        NotImplemented

    def get_deads(self):
        NotImplemented
