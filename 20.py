"""
Студентов надо построить в шеренгу от самого легкого до самого тяжелого. Кто мало весит - тем выдать матпомощь..
При одинаковом весе сначала идет студент с большим ростом (тощий).
"""
def equal(a, b):
    if a[1] < b[1] or (a[1] == b[1] and a[0] > b[0]):
        return -1
    if a[1] > b[1] or (a[1] == b[1] and a[0] < b[0]):
        return 1
    return 0

def quick_sort(a):
    if len(a) < 2:
        return
    barrier = a[0]
    l=[]
    m=[]
    r=[]
    for k in a:
        if equal(k, barrier) == -1:
            l.append(k)
        if equal(k, barrier) == 0:
            m.append(k)
        if equal(k, barrier) == 1:
            r.append(k)
    quick_sort(l)
    quick_sort(r)
    a[:] = l + m + r

n =int(input())
list = [0]*n
for i in range(0, n):
    buf = input().split(" ")
    list[i] = (float(buf[0]), float(buf[1]))

quick_sort(list)
for k in list:
    print("{0:.2f} {1:.3f}".format(k[0], k[1]))
