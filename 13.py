"""Подсчет единиц в двоичном представлении числа"""
x = int(input())
count = 0
for k in bin(x):
    if k == "1":
        count += 1
print(count)
