"""
Рассмотрим игру «Ферзя в угол» для двух игроков.
В левом верхнем углу доски размером N*M находится ферзь,
который может двигаться только вправо-вниз. Игроки по очереди двигают ферзя,
то есть за один ход игрок может переместить ферзя либо по вертикали вниз,
либо по горизонтали вправо, либо во диагонали вправо-вниз.
Выигрывает игрок, который поставит ферзя в правый нижний угол.
Необходимо определить, какой из игроков может выиграть в этой игре
независимо от ходов другого игрока (имеет выигрышную стратегию).
"""
def chessmate_queen(n, m):
    def find(a, i, j):
        for k in range(i + 1, n):
            if  not a[k][j] :
                print(i, j)
                print(k,j)
                return True
        for q in range(j + 1, m):
            if  not a[i][q] :
                print("_",i, j)
                return True
        k = i + 1
        q = j + 1
        while k < n and q < m:
            if  not a[k][q] :
                print("__", i, j)
                return True
            k +=1
            q +=1
        return False

    a = [[None]*m for i in range(0, n)]
    a[n-1][m-1] = False
    count = 0
    for i in reversed(range(0, n)):
        for j in reversed(range(0, m)):
            if a[i][j] is None:
                a[i][j] = find(a, i, j)

    for i in a:
        print(i)

    return a[0][0]


def chessmate_king(n, m):
    def find(a, i, j):
        if  i+1 < n and not a[i+1][j] :
            return True
        if  j+1 < n and not a[i][j+1] :
            return True
        if  j+1 < n and i+1 < n and not a[i+1][j+1] :
            return True
        return False

    a = [[None]*m for i in range(0, n)]
    a[n-1][m-1] = False
    count = 0
    for i in reversed(range(0, n)):
        for j in reversed(range(0, m)):
            if a[i][j] is None:
                a[i][j] = find(a, i, j)

    for i in a:
        print(i)

    return a[0][0]

print("Первый игрок имеет выигрышную стратегию" if chessmate_king(6, 6) else
      "Второй игрок имеет выигрышную стратегию")

