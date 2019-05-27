"""Определение наиболее часто встречаемого числа в последовательности, числа от 0 до 100, такое число одно"""
#dict = {}

n = int(input())
f = [0] * 101
for k in range(0, n):
    a = int(input())
    f[a] += 1
max = 0
maxk = -1
for k in range(0, 101):
    if f[k] > max:
        max = f[k]
        maxk = k
print(maxk)