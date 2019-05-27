"""Среднее арифмитическое последовательности, заканчивающейся 0, не включая"""
a = int(input())
sum = 0
count = 0
while a != 0:
    sum += a
    count += 1
    a = int(input())
print(0 if count == 0 else round(sum/count,2))
