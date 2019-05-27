"""Сколько раз цифра d входит в десятичную запись числа n?"""
inp = input().split()
d = inp[0]
n = inp[1]
count = 0
for s in n:
    if s == d:
        count += 1
print(count)