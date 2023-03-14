N, M, K = map(int, input().split())
edges = [None]

INF = 1

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
    INF += C

E = list(map(int, input().split()))

dp = [None for _ in range(N+1)]
dp[1] = 0

for k in range(K):
    ek = E[k]
    a, b, c = edges[ek]
    if dp[a] is not None:
        if dp[b] is not None:
            dp[b] = min(dp[b], dp[a] + c)
        else:
            dp[b] = dp[a] + c

if dp[N] is None:
    print(-1)
else:
    print(dp[N])
