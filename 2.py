"""Нахождение всех возможных вариантов разбиения шоколадки 3хN по 2 дольки без остатка (N - предполагается четное)
метод грубой силы FIXME"""
n = int(input())
ch = [0] * (n*3)

count = 0


def add_ch(ch, i, j):
    global count
    i, j = find(ch, i, j)
    if i >= n or (i == n-1 and j == 2):
        count += 1
        return
    ch1 = ch[:]
    ch2 = ch[:]
    if j < 2 and ch1[i*3 + j + 1] == 0:
        ch1[i*3 + j] = 1
        ch1[i*3 + j + 1] = 1
        add_ch(ch1, i, j)
    if i+1 < n and ch2[(i+1) * 3 + j] == 0:
        ch2[i*3 + j] = 1
        ch2[(i+1) * 3 + j] = 1
        add_ch(ch2, i, j)

def find(ch, i, j):
    while(i < n):
        if ch[i*3 + j] == 1:
            if j == 2:
                j = 0
                i += 1
            else:
                j += 1
        else:
            return i, j

    return i, j

add_ch(ch, 0, 0)


print(count)