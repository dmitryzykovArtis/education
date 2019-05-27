def is_bracket_correct(str):
    """Проверка скобочной последовательности str
    >>> print(is_bracket_correct("()[]()")) # doctest: +SKIP
    True
    >>> print(is_bracket_correct("(())()")) # doctest: +SKIP
    True
    >>> print(is_bracket_correct("((())]")) # doctest: +SKIP
    False
    >>> print(is_bracket_correct("([])][")) # doctest: +SKIP
    False
    """
    stack = []
    brackets = {"}":"{",
                "]":"[",
                ")":"("}
    for ch in str:
        if ch not in "{[()]}":
            continue
        if ch in "{[(":
            stack.append(ch)
            continue
        if len(stack) == 0:
            return False
        if stack.pop() != brackets[ch]:
            return False
    if len(stack) != 0:
        return False
    return True


def insert_sort(list: list):
    """Сортиировка списка list методом вставки
    >>> a = [5, 2, 1, 4, 3] # doctest: +SKIP
    >>> insert_sort(a) # doctest: +SKIP
    >>> a   # doctest: +SKIP
    [1, 2, 3, 4, 5]
    """
    n = len(list)
    for t in range(1, n):
        k = t
        while k > 0 and list[k-1] > list[k]:
            list[k-1], list[k] = list[k], list[k-1]
            k -= 1

def choise_sort(list: list):
    """Сортировка списка list методом выбора
    >>> a = [5, 2, 1, 4, 3] # doctest: +SKIP
    >>> choise_sort(a) # doctest: +SKIP
    >>> a # doctest: +SKIP
    [1, 2, 3, 4, 5]
    """
    n = len(list)
    for k in range(0, n-1):
        for m in range(1+k, n):
            if list[k] > list[m]:
                list[k], list[m] = list[m], list[k]

def bubble_sort(list: list):
    """Сортировка списка list методом пузырька
    >>> a = [5, 2, 1, 4, 3] # doctest: +SKIP
    >>> bubble_sort(a) # doctest: +SKIP
    >>> a # doctest: +SKIP
    [1, 2, 3, 4, 5]
    """
    n = len(list)
    for k in range (0, n-1):
        for m in range (0, n-1-k):
            if list[m] > list[m+1]:
                list[m], list [m+1] = list[m+1], list[m]

def quick_sort(list: list):
    """Сортировка списка list методом Тони Хоара(быстрая сортировка)
    >>> a = [5, 2, 1, 4, 3] # doctest: +SKIP
    >>> quick_sort(a) # doctest: +SKIP
    >>> a # doctest: +SKIP
    [1, 2, 3, 4, 5]
    """
    n = len(list)
    left = []
    middle = []
    right = []
    if n < 2:
        return
    barrier = list[0]
    for k in list:
        if k < barrier:
            left.append(k)
        elif k == barrier:
            middle.append(k)
        else:
            right.append(k)
    quick_sort(left)
    quick_sort(right)
    list[:] = left + middle + right


def merge_sort(a: list):
    """Сортировка списка list методом слияния
    >>> a = [5, 2, 1, 4, 3]
    >>> merge_sort(a)
    >>> a
    [1, 2, 3, 4, 5]
    """

    def merge(a: list, b: list):
        c = [0]*(len(a) + len(b))
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c[i+j] = a[i]
                i += 1
            else:
                c[i+j] = b[j]
                j += 1
        while i < len(a):
            c[i+j] = a[i]
            i += 1
        while j < len(b):
            c[i + j] = b[j]
            j += 1
        return c

    n = len(a)
    if n < 2:
        return
    middle = n//2
    l = [a[i] for i in range(0, middle)]
    r = [a[i] for i in range(middle, n)]
    merge_sort(l)
    merge_sort(r)
    c = merge(l, r)
    for i in range (0, n):
        a[i] = c[i]


if __name__ == "__main__":
    import sys
    import timeit
    import random
    sys.setrecursionlimit(100000)
    data1 = [random.randint(0,2500) for k in range(0, 500000)]
    data2 = data1[:]
    data3 = data1[:]
    data4 = data1[:]
    data5 = data1[:]
    #print(timeit.timeit("bubble_sort(data1)", setup="from __main__ import bubble_sort, data1", number=1))
    #print(timeit.timeit("insert_sort(data2)", setup="from __main__ import insert_sort, data2", number=1))
    #print(timeit.timeit("choise_sort(data3)", setup="from __main__ import choise_sort, data3", number=1))
    print(timeit.timeit("quick_sort(data4)", setup="from __main__ import quick_sort, data4", number=1))
    print(timeit.timeit("merge_sort(data5)", setup="from __main__ import merge_sort, data5", number=1))

    #import doctest
    #doctest.testmod(verbose=True)

    x, y, r =  input().split(" ")
    


