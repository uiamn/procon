N, M, Q = map(int, input().split())
# table[L][R] = 都市 L から都市 R を走る電車の総数
table = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    L, R = map(int, input().split())
    table[L][R] += 1

# 累積和を求めておく
S = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + table[i][j]

for _ in range(Q):
    p, q = map(int, input().split())
    ans = S[N][q] - S[p-1][q] - S[N][0] + S[p-1][0]
    print(ans)
