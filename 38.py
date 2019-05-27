"""Реализация кучи"""
class Heap:
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)
        self.__up()

    def __up(self):
        i = len(self.list) - 1
        while i > 0 and self.list[(i-1)//2] < self.list[i]:
            self.list[(i - 1) // 2], self.list[i] = self.list[i], self.list[(i-1)//2]
            i = (i - 1) // 2

    def __down(self):
        i = 0
        while (2*i+1 < len(self.list) and self.list[i] < self.list[2*i+1])\
                or (2*i+2 < len(self.list) and self.list[i] < self.list[2*i+2]):
            if 2*i+2 < len(self.list) and self.list[2*i+1] < self.list[2*i+2]:
                self.list[i], self.list[2 * i + 2] = self.list[2 * i + 2], self.list[i]
                i = 2 * i + 2
            else:
                self.list[i], self.list[2 * i + 1] = self.list[2 * i + 1], self.list[i]
                i = 2 * i + 1

    def get(self, i):
        return self.list.get(i)

    def size(self):
        return len(self.list)

    def pop(self):
        buf = self.list[0]
        self.list[0], self.list[len(self.list) - 1] = self.list[len(self.list) - 1], self.list[0]
        self.list.pop()
        self.__down()
        return buf

    def __str__(self):
        return str(self.list)


h = Heap()
h.push(5)
print(h)
h.push(2)
print(h)
h.push(4)
print(h)
h.push(1)
print(h)
h.push(3)
print(h)
print(h.pop())
print(h)
print(h.pop())
print(h)
print(h.pop())
print(h)
print(h.pop())
print(h)
print(h.pop())
print(h)
