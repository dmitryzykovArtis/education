"""Нахождение наибольшей общей подпоследовательности"""
def lcs(a,b):
    n = len(a)
    m = len(b)
    F = [[0]*(m+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i][j-1],F[i-1][j])
    return F[n][m]

print(lcs('1123235', '111351'))
































"""Нахождение наибольшей общей подпоследовательности

def lcs(a, b):
    n = len(a)
    m = len(b)
    answ = ''
    F = [[0]*(m+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                F[i][j] = F[i-1][j-1] + 1
                if F[i][j] > F[i-1][j] and F[i][j] > F[i][j-1]:
                    answ = answ + a[i - 1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])

    for i in F:
        print(i)
    print(answ)

lcs('1123235', '111351')
"""
