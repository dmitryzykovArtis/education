"""Проверка на Гамильтонов граф"""
n, m = map(int, input().split(" "))
G = [[] for i in range(n)]
for i in range(m):
    k, v = map(int, input().split(" "))
    G[k].append(v)
    G[v].append(k)

def is_gam_circle(G):

    res = dps(G, tuple(), 0)
    if res is not None:
        print(" ".join(map(str,res)))

def dps(G, used, start):
    neibours = len(G[start])
    used = used + (start,)
    for v in G[start]:
        if v == used[0] and len(used) == len(G):
            return used
        if v in used:
            continue
        res = dps(G, used, v)
        if res is not None:
            return res
    return None

is_gam_circle(G)
