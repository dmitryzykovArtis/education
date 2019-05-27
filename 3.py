"""Определение прямого, тупоугольного, остроуголього, несуществующего треугольника по длинне трех его сторон"""
x = int(input())
y = int(input())
z = int(input())
if z >= x and z >= y:
    c = z
    a = x
    b = y
elif x >= z and x >= y:
    c = x
    a = z
    b = y
else:
    c = y
    a = z
    b = x

if c >= a + b:
    print("impossible")
elif c*c > a*a + b*b:
    print("obtuse")
elif c*c == a*a + b*b:
    print("right")
elif c*c < a*a + b*b:
    print("acute")