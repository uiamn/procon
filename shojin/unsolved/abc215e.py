N = int(input())
table = {chr(65+n): (1 << n) for n in range(10)}
S = [None] + [ord(c)-65 for c in input()]

dp = [[[0 for _ in range(N+1)] for _ in range(10)] for _ in range(1 << 10)]
po = [1 << i for i in range(10)]

# dp[Set][x][i]: i 日目までのコンテストの出方で，最後のコンテストが AxC であり，かつ今までに出場したことのあるコンテストの集合は Set である．

dp[S[1]][S[1]][1] = 1

for n in range(2, N+1):
    i = S[n]
    c = 1 << i

    for s in range(1 << 10):
        if s & c == 0:
            dp[s][i][n] = 0
        else:
            dp[s][i][n] = dp[s][i][n-1]

            for j in range(10):
                dp[s][i][n] += dp[s-c][j][n-1]

ans = 0
for s in range(1, 1<<10):
    for i in range(10):
        ans += dp[s][i][N]

print(ans)
