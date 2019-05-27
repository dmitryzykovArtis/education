"""Скалярое произведение двух векторов a, b размерностью n"""
def dot_product(n, a, b):
    sum = 0
    for i in range(0, n):
        sum += a[i]*b[i]
    return sum

#print(dot_product(3, [1, 2, 3], [4, 5, 6]))
