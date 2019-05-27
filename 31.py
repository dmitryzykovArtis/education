
"""Нахождение наибольшей возрастающей подпоследовательости"""

def lgs(a):
    n = len(a)
    F = [0] * (n)
    F[0] = 1
    for i in range(1, n):
        m = 0
        for j in range(0, i):
             if a[i] > a[j] and F[j] > m:
                 m = F[j]
             F[i] = m + 1

    print(F)
    return F[n-1]

print(lgs("132546879"))

