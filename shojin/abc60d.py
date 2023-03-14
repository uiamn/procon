N, W = map(int, input().split())
ws = [None]
w1 = None
vs = [None]

for i in range(N):
    w, v = map(int, input().split())
    if i == 0:
        ws.append(0)
        w1 = w
    else:
        ws.append(w-w1)
    vs.append(v)

# dp[i][j][k] = 1 から i まで j 個選んで物の重さが k 以下になるやうな物の入れ方であって価値の総和が最大となるものの価値の総和
dp = [[[0 for _ in range(4*(j+1)+1)] for j in range(i+2)] for i in range(N+1)]


for i in range(3):
    dp[1][1][i] = vs[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        for k in range(4*j+1):
            dp[i][j][k] = dp[i-1][j][k]
            for l in range(k-ws[i]+1):
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][l] + vs[i])

ans = 0
for j in range(1, N+1):
    for k in range(4*j+1):
        if j*w1 + k <= W:
            ans = max(ans, dp[N][j][k])

print(ans)
