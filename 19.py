"""
Напечатайте входную последовательность натуральных чисел, отсортировав ее по возрастанию сначала единиц,
 потом десятков, потом сотен и тп.
"""


def equal(a, b):
    for i in range(0, min(len(a), len(b))):
        if a[-1-i] < b[-1-i]:
            return -1
        if a[-1-i] > b[-1-i]:
            return 1
    if len(a) < len(b):
        return -1
    if len(a) > len(b):
        return 1
    return 0

def quick_sort(a):
    if len(a) < 2:
        return
    barrier = a[0]
    l=[]
    r=[]
    m=[]
    for i in range(0, len(a)):
        if equal(a[i], barrier) == -1:
            l.append(a[i])
        if equal(a[i], barrier) == 0:
            m.append(a[i])
        if equal(a[i], barrier) == 1:
            r.append(a[i])
    quick_sort(l)
    quick_sort(r)
    a[:] = l + m + r

n = int(input())
a = input().split(" ")
quick_sort(a)
print(" ".join(a))



