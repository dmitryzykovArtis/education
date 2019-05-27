"""Графы. Добавление в связный список, Поиск в глубину, Поиск в ширину"""

G = {}


class Stack:
    """Реализация простого стека без контроля заполнености
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> print(stack.is_empty())
        False
        >>> print(stack.pop())
        3
        >>> print(stack.pop())
        2
        >>> print(stack.pop())
        1
        >>> print(stack.is_empty())
        True
        """
    class Element:
        def __init__(self, nxt, value):
            self.nxt = nxt
            self.value = value

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        self.head = Stack.Element(self.head, value)

    def pop(self):
        buf = self.head.value
        self.head = self.head.nxt
        return buf


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


def add(g):
    n = int(input())
    for i in range(0, n):
        x, y = map(int, input().split(" "))
        for k, v in (x,y),(y,x):
            if k in g:
                g[k].add(v)
            else:
                g[k] = {v}


def depth_first_search(g, start):
    stack = Stack()
    used = set()
    stack.push(start)
    while not stack.is_empty():
        v = stack.pop()
        if v in used:
            continue
        for i in G[v]:
            if i not in used:
                stack.push(i)
        used.add(v)
        print(v)

def bread_first_search(g, start):
    queue = Queue()
    used = set()
    queue.push(start)
    used.add(start)
    while not queue.is_empty():
        v = queue.pop()
        for i in G[v]:
            if i not in used:
                queue.push(i)
                used.add(i)
        print(v)
if __name__ == "__main__":
    add(G)
    depth_first_search(G, 1)


"""
Для тестирования стека и очереди:
import doctest
doctest.testmod(verbose = True)
"""


