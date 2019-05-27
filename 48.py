"""Поиск кратчайшего пути между 0 и всеми узлами невзвешенного графа"""


class Queue:
    """Реализация простой очереди без контроля заполнености
    >>> queue = Queue()
    >>> queue.push(1)
    >>> queue.push(2)
    >>> queue.push(3)
    >>> print(queue.is_empty())
    False
    >>> print(queue.pop())
    1
    >>> print(queue.pop())
    2
    >>> print(queue.pop())
    3
    >>> print(queue.is_empty())
    True
    """
    class Element:
        def __init__(self, nxt, value):
            self.nxt = nxt
            self.value = value

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        if self.is_empty():
            self.tail = self.head = Queue.Element(None, value)
        else:
            self.tail.nxt = Queue.Element(None, value)
            self.tail = self.tail.nxt

    def pop(self):
        buf = self.head.value
        self.head = self.head.nxt
        return buf

queue = Queue()

n, m = map(int, input().split(" "))
x = 0

G = [[] for i in range(n)]
path = [-1]*n
for i in range(m):
    k, v = map(int, input().split(" "))
    G[k].append(v)
    G[v].append(k)

def find_path(G, x, queue, path):
    path[x] = 0
    queue.push(x)
    while not queue.is_empty():
        x = queue.pop()
        for i in G[x]:
            if path[i] == -1:
                path[i] = path[x] + 1
                queue.push(i)

find_path(G, x, queue, path)

for i in path:
    print(i)



