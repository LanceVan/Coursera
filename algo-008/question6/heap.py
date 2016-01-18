class Heap:

    def __init__(self):
        self.value = [None]

    def check(self, valuex, valuey):
        return valuex < valuey

    def size(self):
        return len(self.value) - 1

    def insert(self, data):
        self.value.append(data)
        k = self.size()
        while k != 1:
            if self.check(self.value[k], self.value[k // 2]):
                self.value[k], self.value[k // 2] = self.value[k // 2], self.value[k]
                k //= 2
            else:
                break

        return self.value

    def extract(self):
        top = self.value[1]
        self.value[1] = self.value[self.size()]
        self.value.pop()
        k = 1
        while 2 * k <= self.size():
            if 2 * k == self.size():
                if self.check(self.value[2 * k], self.value[k]):
                    self.value[2 * k], self.value[k] = self.value[k], self.value[2 * k]
                break
            if self.check(self.value[2 * k], self.value[2 * k + 1]):
                if self.check(self.value[2 * k], self.value[k]):
                    self.value[2 * k], self.value[k] = self.value[k], self.value[2 * k]
                    k *= 2
                else:
                    break
            else:
                if self.check(self.value[2 * k + 1], self.value[k]):
                    self.value[2 * k + 1], self.value[k]= self.value[k], self.value[2 * k + 1]
                    k = k * 2 + 1
                else:
                    break

        return top
