"""
Количество различных комбинаций размена суммы money монетами из списка coins
"""
def make_exchange(money, coins):
    count = [[0] * (money+1) for coins in range(0, len(coins) + 1)]
    coins.sort()
    if len(coins) == 0:
        return 0
    if money < coins[0]:
        return 0
    for i in range(1, len(coins)+1):
        coinsbag = coins[0:i]
        count[i][0] = 1
        for j in range(coins[0], money + 1):
            count[i][j] = count[i-1][j] + count[i][j - coinsbag[-1]]

    return count[len(coins)][money]

