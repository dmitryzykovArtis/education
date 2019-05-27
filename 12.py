"""Побитовый XOR двух шестнадцатеричных чисел"""
inp = input().split(" ")
x = int(inp[0], 16)
y = int(inp[1], 16)
print(hex(x^y)[2:])