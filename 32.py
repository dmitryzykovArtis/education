"""Расстояние Ливенштейна"""
def livenshtein(a, b):
    n = len(a)
    m = len(b)
    F = [[(i+j) if i*j == 0 else 0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j], F[i][j-1], F[i-1][j-1]) + 1
    for i in F:
        print(i)
    return F[n][m]

print(livenshtein("qwerty", "reeety"))
