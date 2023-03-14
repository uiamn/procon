N, M = map(int, input().split())
A = [None] + list(map(int, input().split()))

dp = [set([]) for _ in range(N+1)]
dp[1] = set(range(1, M+1))

for k in range(1, M+1):
    a = dp[A[k]]
    b = dp[A[k]+1]

    if k in a:
        a -= set([k])
        b |= set([k])
    elif k in b:
        b -= set([k])
        a |= set([k])

    dp[A[k]+1] = a
    dp[A[k]] = b


S = [None for _ in range(M+1)]

for n, d in enumerate(dp):
    for s in d:
        S[s] = n

for i in range(1, M+1):
    print(S[i])
