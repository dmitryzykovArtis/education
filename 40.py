"""Определение простоты графа по его матрице смежости"""
n = int(input())
F = [list(map(int, input().split(" "))) for i in range(n)]
def is_simple(F):
    m = len(F)
    for i in range(m):
        for j in range(m):
            if (i == j and F[i][j] != 0)\
                    or F[i][j] > 1\
                    or F[i][j] !=  F[j][i]:
                return False
    return True
print("YES" if is_simple(F) else "NO")

