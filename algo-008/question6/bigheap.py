from heap import Heap

class BigHeap(Heap):

    def __init__(self):
        Heap.__init__(self)

    def check(self, valuex, valuey):
        return valuex > valuey
