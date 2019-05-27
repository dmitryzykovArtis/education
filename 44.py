"""Топологическая сортировка"""
n, m = map(int, input().split(" "))
G = [[] for i in range(n)]
for i in range(m):
    k, v = map(int, input().split(" "))
    G[k].append(v)

def dfs(G, start, path, circle_check):
    neibours_count = len(G[start])
    circle_check.append(start)
    for i in range(neibours_count):
        v = G[start][i]
        if v in path:
            continue;
        if v in circle_check:
            return True
        res = dfs(G,v, path, circle_check)
        if res:
            return True
    path.append(start)
    return False

def topologic(G):
    n = len(G)
    path = []
    for i in range(n):
        if i not in path:
            circle_check = []
            res = dfs(G, i, path, circle_check)
            if res:
                print("NO")
                return
    print(" ".join(map(str,path[::-1])))

topologic(G)





