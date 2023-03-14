N, M, K = map(int, input().split())

MOD = 998244353

minvtable = [
    None,
    1,
    499122177,
    332748118,
    748683265,
    598946612,
    166374059,
    855638017,
    873463809,
    443664157,
    299473306
]

minv = minvtable[M]

# dp[k][n] = ルーレットを k 回回すときにマス n にゐる確率
dp = [[None for __ in range(N+1)] for _ in range(K+1)]

dp[0][0] = 1
for i in range(1, N+1):
    dp[0][i] = 0

for k in range(1, K+1):
    for n in range(N+1):
        p = 0
        for m in range(1, M+1):
            if 0 <= n-m:
                p += dp[k-1][n-m] * minv

        if N > n >= N - M + 1:
            for j in range(n-(N-M+1)+1):
                if 1 <= N-j-1:
                    p += dp[k-1][N-j-1] * minv

        dp[k][n] = p % MOD

ans = 0
for k in range(1, K+1):
    ans += dp[k][n]
    ans %= MOD

print(ans)
