"""Блондинка Даша любит решать кроссворды на латинском языке, пользуясь орфографическим словарем.
Часто Даша отгадывает последние буквы слова и долго ищет каким словам подходит такая концовка.
Она мечтает о словаре, где бы слова были разбиты на главы по количеству букв в слове и написаны задом наперед.
Помогите ей составить такой словарь по заданному орфографическому словарю латинском языка.

3
eucharis
fittonia
tagetes
"""

def merge_sort(a):

    def merge(a, b):
        i = 0
        j = 0
        c = [0]*(len(a)+len(b))
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
            c[i+j] = b[j]
            j += 1
        return c

    n = len(a)
    if n < 2:
        return
    l = a[0:n//2]
    r = a[n//2: n]
    merge_sort(l)
    merge_sort(r)
    a[:] = merge(l, r)


dict = [0]*17
for i in range(0, 17):
    dict[i] = []

n = int(input())
for i in range(0, n):
    s = input()
    dict[len(s)].append(s[::-1]+" "+s)

for i in range(0, 17):
    if len(dict[i]) == 0:
        continue
    print(i)
    merge_sort(dict[i])
    for k in dict[i]:
        print(k)



