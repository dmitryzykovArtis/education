"""Алгоритм Кнута-Морриса-Пратта"""

def pref(a):
    n = len(a)
    F = [0]*n
    p = 0
    for i in range(1, n):
        while p != 0 and a[i] != a[p]:
            p = F[p]
        if a[i] == a[p]:
            p += 1
        F[i] = p
    return F

print(pref("abadabafabadaba"))

def kmp(s, t):
    index = -1
    k = 0
    F = pref(s)
    for i in range(0, len(t)):
        while k > 0 and s[k] != t[i]:
            k = F[k-1]
        if s[k] == t[i]:
            k += 1
        if k == len(s):
            index = i - k + 1
            print(index)
            k = F[k - 1]
    return index
print(kmp("abadaba", "abadabadabafabacabadabafabadaba"))


