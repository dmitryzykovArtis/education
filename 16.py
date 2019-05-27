"""Некоторые скобочные структуры правильные, другие — неправильные.
 Ваша задача — определить правильная ли скобочная структура."""
str = input()
stack = []
res = True
for s in str:
    if s not in "()":
        continue
    if s in "(":
        stack.append(s)
    if len(stack) == 0:
        res = False
        break
    if s == ")" and stack.pop() != "(":
        res = False
if len(stack) != 0:
    res = False
print("YES" if res else "NO")
