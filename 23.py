"""
Стандартная задача на нахождение количества маршрутов кузнечика прыгающего по клеткам
 c 1 по n
"""

def kuz_one_two(n):
    """Стандартная задача на нахождение маршрута для прыжков +1 и +2(числа фибоначи)"""
    K = [0] * (n+1)
    print(len(K))
    K[0] = 0
    K[1] = 1
    for i in range(2, n+1):
        K[i] = K[i-1] + K[i-2]
    return K[n]

def kuz_one_two_three(n):
    """Задача на нахождение маршрута для прыжков +1 и +2 и +3("трибоначи")"""
    K = [0] * (n+1)
    K[0] = 0
    K[1] = 1
    K[2] = 1
    for i in range(3, n+1):
        K[i] = K[i-1] + K[i-2] + K[i-3]
    return K[n]

def kuz_one_two_multi_three(n):
    """Задача на нахождение маршрута для прыжков +1 и +2 и *3("трибоначи")"""
    K = [0] * (n+1)
    K[0] = 0
    K[1] = 1
    K[2] = 1

    """
    Стоит отдельно уточнять считать ли прыжок +2 и *3 c клетки 1 до 3
    различными маршрутами, как по кратным ребрам графа. В данной реализации принимаем
    переходы с 1 до 3 за единый маршрут
    """
    K[3] = 2
    for i in range(4, n + 1):
        K[i] = K[i - 1] + K[i - 2] + ( K[i//3] if i%3 == 0 else 0 )
    return K[n]

def kuz_one_two_price(n):
    """Задача нахождения минимальной стоимости маршрута при шагах +1 и +2"""
    MAX_PRICE = 9999
    K = [0]*(n+1)
    price = [1]*(n+1)
    K[0] = MAX_PRICE
    K[1] = 0
    for i in range(2, n+1):
        #K[i] = min(K[i - 1], K[i - 2]) + price[i]
        K[i] = (K[i - 1] if K[i - 1] < K[i - 2] else K[i - 2]) + price[i]
    return K[n]

def kuz_one_two_multi_three_price(n):
    """Задача нахождения минимальной стоимости маршрута при шагах +1, +2, *3"""
    price = [1] * (n+1)
    MAX_PRICE = 9999
    K = [0] * (n + 1)
    K[0] = MAX_PRICE
    K[1] = 1
    K[2] = 2
    for i in range(3, n + 1):
        K[i] = min(K[i - 1], K[i - 2], K[i // 3] if i % 3 == 0 else MAX_PRICE) + price[i]
    return K[n]

def kuz_one_two_multi_three_price_prev(n):
    """Задача нахождения минимальной стоимости маршрута при шагах +1, +2, *3,
    с выводом маршрута
    """
    prev = [0] * (n + 1)
    price = [1] * (n + 1)
    MAX_PRICE = 9999
    K = [0] * (n + 1)
    K[0] = MAX_PRICE
    K[1] = 0
    K[2] = 1
    for i in range(2, n + 1):
        multi = K[i // 3] if i % 3 == 0 else MAX_PRICE
        if K[i - 1] < K[i - 2] and K[i - 1] < multi:
            min = K[i - 1]
            prev[i] = i - 1
        elif K[i - 2] < K[i - 1] and K[i - 2] < multi:
            min = K[i - 2]
            prev[i] = i - 2
        else:
            min = multi
            prev[i] = i // 3
        K[i] = min + price[i]
    i = n
    s = str(n)
    while i != 1:
        s = str(prev[i]) + " " +  s
        i = prev[i]
    s += " min: " + str(K[n])
    return s

print(kuz_one_two_multi_three_price_prev(10))