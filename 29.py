"""
Задача о рюкзаке (дискретная)
"""
n = int(input())
m = int(input())
price = [0]*(n+1)
weight = [0]*(n+1)
value = [[0]*(n+1) for i in range(0, m+1)]
for i in range(1, n+1):
    weight[i] = int(input())
    price[i] = int(input())

for i in range(1, n+1):
    for j in range(1, m+1):
        if weight[i] > j:
            value[j][i] = value[j][i - 1]
            continue
        value[j][i] = (value[j][i - 1] if value[j][i - 1] > value[j-weight[i]][i-1] + price[i]
                       else value[j - weight[i]][i - 1] + price[i])

print(value[m][n])

