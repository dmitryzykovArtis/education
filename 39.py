"""Нахождение количества ребер графа по матрице смежности"""
n = int(input())
count = 0


def sum(x):
    global count
    x = int(x)
    if x > 0:
        count += x
    return x


for i in range(n):
    for j in input().split(" "):
        sum(j)
print(count//2)
