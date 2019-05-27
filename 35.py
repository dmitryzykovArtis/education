"""Префикс функция"""

def pref(a):
    n = len(a)
    F = [0]*n
    k = 0
    for i in range(1, n):
        while k != 0 and a[k] != a[i]:
            k = F[k]
        if a[k] == a[i]:
            k += 1
        F[i] = k
    return F
print(pref("abadabafabadaba"))



