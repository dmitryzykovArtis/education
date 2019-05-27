"""Нахождение числа НОД алгоритмом Евклида"""

def evkl_diff(a, b):
    if a == b:
        return a
    if a > b:
        return evkl_diff(a - b, b)
    if a < b:
        return evkl_diff(a, b - a)

def evkl_div(a, b):
    if a == 0:
        return b
    if a > b:
        return evkl_div(a % b, b)
    if a < b:
        return evkl_div(b % a, a)

a = int(input())
b = int(input())

print(evkl_div(a, b))