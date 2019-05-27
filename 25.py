"""
Вам даны 2 координаты 2 клеток на шахматном поле.
Нужно ответить на вопрос, можно ли попасть из одной клетки в другую
за не более чем 2 хода конем. В случае, если попасть возможно, надо
вывести количество ходов, за которое это можно сделать. Если попасть невозможно,
следует вернуть -1.
"""
def is_pos(x1, y1, x2, y2, t, count):
    """Не оптимальное решение рекурсией, надо использовать массив по хорошему или находить минимум
     из каунт"""
    #print(x1,x2,y1,y2)
    if t < 0:
        return False
    if not (0 <= x1 < 8 and 0 <= y1 < 8):
        return False
    if (x1, y1) == (x2, y2):
        return count
    t -=1
    count += 1
    return (is_pos(x1 - 1, y1 - 2, x2, y2, t, count) or
            is_pos(x1 + 1, y1 - 2, x2, y2, t, count) or
            is_pos(x1 + 2, y1 - 1, x2, y2, t, count) or
            is_pos(x1 + 2, y1 + 1, x2, y2, t, count) or
            is_pos(x1 + 1, y1 + 2, x2, y2, t, count) or
            is_pos(x1 - 1, y1 + 2, x2, y2, t, count) or
            is_pos(x1 - 2, y1 + 1, x2, y2, t, count) or
            is_pos(x1 - 2, y1 - 1, x2, y2, t, count)
            )
x1 = int(input()) - 1
y1 = int(input()) - 1
x2 = int(input()) - 1
y2 = int(input()) - 1



res = is_pos(x1, y1, x2, y2, 2, 0)

print( -1 if res is False else res)