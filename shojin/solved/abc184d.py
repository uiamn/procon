from fractions import Fraction

A, B, C = map(int, input().split())

# dp[i][j][k] = 金貨，銀貨，銅貨がそれぞれ i, j, k 枚あるときに，操作修了までの操作回数の期待値
# 求める値 = dp[A][B][C]
dp = [[[None for _ in range(101)] for _ in range(101)] for _ in range(101)]

for i in range(101):
    for j in range(101):
        dp[100][i][j] = 0.0
        dp[i][100][j] = 0.0
        dp[i][j][100] = 0.0

for a in range(99, A-1, -1):
    for b in range(99, B-1, -1):
        for c in range(99, C-1, -1):
            a_prod = a / (a+b+c)
            b_prod = b / (a+b+c)
            c_prod = c / (a+b+c)

            x = dp[a+1][b][c] * a_prod
            x += dp[a][b+1][c] * b_prod
            x += dp[a][b][c+1] * c_prod
            dp[a][b][c] = x + 1

print(dp[A][B][C])
