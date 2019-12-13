class IAllocatorId:
    allocated = False

    def __init__(self, p=None, n=None):
        self.prev = p
        self.next = n

    def get(self):
        NotImplemented

    def back(self, n):
        NotImplemented

    def get_alives(self):
        NotImplemented

    def get_deads(self):
        NotImplemented
