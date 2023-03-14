N, K = map(int, input().split())
A = list(map(int, input().split()))

"""
dp[i][0] 石が残り i 個のときに高橋くんが次に石を取る場合において高橋くんが取れる最大個数
dp[i][1] 石が残り i 個のときに青木くんが次に石を取る場合において高橋くんが取れる最大個数
"""
dp = [[0, N+1] for _ in range(N+1)]

dp[0][1] = 0
dp[1][0] = 1
dp[1][1] = 0

for i in range(2, N+1):
    for a in A:
        if i-a >= 0:
            dp[i][0] = max(dp[i][0], dp[i-a][1] + a)
            dp[i][1] = min(dp[i][1], dp[i-a][0])

print(dp[N][0])
