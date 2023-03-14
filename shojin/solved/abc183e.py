MOD = 10 ** 9 + 7

H, W = map(int, input().split())
S = [input() for _ in range(H)]

# dp[i][j][k] = マス (i, j) に直前の移動が k (0: 右移動， 1: 下移動， 2: 右下移動) で到達できる通り数
dp = [[[0, 0, 0] for _ in range(W+1)] for _ in range(H+1)]

if S[1-1][2-1] == '.':
    dp[1][2][0] = 1

if S[2-1][1-1] == '.':
    dp[2][1][1] = 1

if S[2-1][2-1] == '.':
    dp[2][2][2] = 1

for i in range(1, H+1):
    for j in range(1, W+1):
        if S[i-1][j-1] == '#':
            continue

        if i == 1 and j == 1:
            continue
        elif i == 1 and j == 2:
            continue
        elif i == 2 and j == 1:
            continue

        dp[i][j][0] = (sum(dp[i][j-1]) + dp[i][j-1][0]) % MOD
        dp[i][j][1] = (sum(dp[i-1][j]) + dp[i-1][j][1]) % MOD
        if i != 2 or j != 2:
            dp[i][j][2] = (sum(dp[i-1][j-1]) + dp[i-1][j-1][2]) % MOD

print(sum(dp[H][W]) % MOD)
