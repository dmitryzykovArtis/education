"""Нахождение числа фибоначи методом динамического программирования"""
def fib_down(n):
    MAX_POSSIBLE_N = 10000
    F = [-1] * MAX_POSSIBLE_N
    def fib_down_rec(n):
        if n <= 1:
            return n
        if F[n] == -1:
            F[n] = fib_down_rec(n - 1) + fib_down_rec(n - 2)
        return F[n]
    return fib_down_rec(n)


def fib_up(n):
    F = [-1]*(n+1)
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]

print(fib_down(100))