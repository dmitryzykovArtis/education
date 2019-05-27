"""Напечатайте входную строку, отсортировав ее по возрастанию ASCII кода символов.
Строка, заканчивающаяся точкой, длиной не более 1000 символов.
Точку сортировать не нужно. Все, что находится после первой точки - игнорировать.
"""

def quick_sort(a):
    if len(a) < 2:
        return
    barrier = a[0]
    l=[]
    r=[]
    m=[]
    for i in range(0, len(a)):
        if a[i] < barrier:
            l.append(a[i])
        if a[i] == barrier:
            m.append(a[i])
        if a[i] > barrier:
            r.append(a[i])
    quick_sort(l)
    quick_sort(r)
    a[:] = l + m + r

str = input().split(".")
string = list(str[0])
quick_sort(string)

print("".join(string)+".")

"""
str = list(input())
pi = -1
for i in range(0, len(str)):
    if str[i] == ".":
        pi = i
        break

for i in range(0, pi-1):
    for j in range(1, pi - i):
        if str[j-1] > str[j]:
            str[j-1], str[j] = str[j], str[j-1]

print("".join(str))
"""