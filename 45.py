"""Проверка на биполярный граф (не ориентированный)"""
n, m = map(int, input().split(" "))
G = [[] for i in range(n)]
for i in range(m):
    k, v = map(int, input().split(" "))
    G[k].append(v)
    G[v].append(k)

used = [False]*n
color = [0]*n

def dfs(G, start, used, color):
    used[start] = True
    neibours_number = len(G[start])
    for i in range(neibours_number):
        v = G[start][i]
        if color[start] == color[v] and v != start:
            return True
        if used[v]:
            continue
        color[v]=-color[start]
        res = dfs(G, v, used, color)
        if res:
            return True
    return False

res = False
for i in range(n):
    if not used[i]:
        color[i] = -1
        res = dfs(G, i, used, color)
        if res:
            print("NO")
            break
if not res:
    answer = []
    for i in range(n):
        if color[i] == -1:
            answer.append(str(i))
    print(" ".join(answer))



