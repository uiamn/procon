def dfs(n, coin_types):
    if len(coin_types) == 0:
        return 1
    elif coin_types[-1] > n:
        return dfs(n, coin_types[:-1])
    else:
        return dfs(n, coin_types[:-1]) + dfs(n-coin_types[-1], coin_types)


print(dfs(200, [2, 5, 10, 20, 50, 100, 200]))
