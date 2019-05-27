""" Дан ориентированный граф. Вершины пронумерованы от 0.
Трeбуется с помощью обхода в глубину проверить является ли граф
ацикличным.

Формат входных данных
На вход программе в первой строке подаются через пробел два числа:
N (2 <= N <= 1000) - число вершин в графе и
M (1 <= M <= 20000) - число ребер.
В следующих M строках задаются ребра, по два числа в каждой строке
- номера соединенных вершин (соответствующее ребро идет
из первой вершины во вторую).

Формат выходных данных
Требуется распечатать номера вершин, задающих цикл в графе
 если он существует. Номера вершин нужно вывести в порядке следования по циклу. Если циклов несколько вывести любой. Если граф ацикличный вывести строку "YES" без кавычек. """

n, m = list(map(int, input().split(" ")))

start = 0
answ = []
path = []
G = [[]]*n
for i in range(n):
    G[i] = []
for i in range(m):
    k, v = map(int,input().split(" "))
    G[k].append(v)

"""Можно сделать при помощи стека, но в этот раз рекурсивно"""



def dfs(G, start, used, path):

    for i in range(len(G[start])):
        v = G[start][i]
        if not used[v]:
            used[v] = True
            path.append(v)
            circle = dfs(G, v, used, path)
            if circle:
                return circle
            else:
                path.pop()
        else:
            if v in path:
                path.append(v)
                used[start] = True
                return True
    used[start] = True
    return False

def is_circle(G):
    used = [False]*n

    for i in range(len(G)):
        path = []
        if used[i]:
            continue
        path.append(i)
        circle = dfs(G, i, used, path)
        if circle:
            i = len(path)-2
            answ = ""
            while path[i] != path[-1]:
                answ = str(path[i])+ " " + answ
                i -= 1
            answ = str(path[i]) + " " + answ
            return answ
    return "YES"

print(is_circle(G))









