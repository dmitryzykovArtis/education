"""Максимальный четный элемент последовательности, заканчивающейся 0, не включая"""
a = int(input())
max = 0
while a != 0:
    if a%2 == 0 and a > max:
        max = a
    a = int(input())
print(max)