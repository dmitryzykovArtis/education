n, m = map(int, input().split(" "))
x1, y1 = map(int, input().split(" "))
x2, y2 = map(int, input().split(" "))
start = x1*m + y1
finish = x2*m + y2


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

block = [[" "]*n for j in range(m)]
for i in range(n):
    block[i] = list(input())

G = [[] for i in range(n*m)]

for i in range(n):
    for j in range(m):
        if block[i][j] == "X":
            continue
        for x, y in (i+1,j),(i,j+1),(i-1,j),(i,j-1):
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if block[x][y] == "X":
                continue
            G[i*m+j].append(x*m+y)

path = [-1]*(n*m)



def bfs(G, start, path, queue):
    queue.push(start)
    path[start] = 0
    while not queue.is_empty():
        x = queue.pop()
        for i in G[x]:
            if path[i] == -1:
                path[i] = path[x] + 1
                queue.push(i)

if block[x1][y1] == "X" or block[x2][y2] == "X":
    print("INF")
else:
    bfs(G, start, path, queue)
    print(path[finish] if path[finish] != -1 else "INF")

