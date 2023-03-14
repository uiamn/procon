def modsum(l, MOD):
    s = 0
    for ll in l:
        s += ll
        s %= MOD

    return s


MOD = 998244353
N, M, K = map(int, input().split())
broken_bridges = []

for _ in range(M):
    u, v = map(int, input().split())
    broken_bridges.append((u, v))

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
dp[0][1] = 1
tmpsum = 1

for k in range(1, K+1):
    tmpsum = modsum(dp[k-1], MOD)
    for n in range(1, N+1):
        dp[k][n] = tmpsum - dp[k-1][n]

    for (u, v) in broken_bridges:
        dp[k][u] = (dp[k][u] - dp[k-1][v]) % MOD
        dp[k][v] = (dp[k][v] - dp[k-1][u]) % MOD

print(dp[K][1] % MOD)
