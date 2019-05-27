"""
Нахождение первого номера элемента последовательности чисел "Трибоначи" превосходящего заданное число
"""
x = int(input())
trib = [0, 0, 1]
while trib[len(trib) - 1] <= x:
    trib.append(trib[len(trib) - 1] + trib[len(trib) - 2] + trib[len(trib) - 3])
print(len(trib) - 1)