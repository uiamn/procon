N, W = map(int, input().split())
ws = []
vs = []

for _ in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

# dp[i-1][j] = 1 から i までの物で重さが w_1+j 以下になるやうな物の入れ方であって価値の総和が最大となるものの価値の総和
dp = [[0 for _ in range((i+1)*3)] for i in range(N)]

for i in range(min(3, W-ws[0])):
    dp[0][i] = vs[0]

for i in range(1, N+1):
    for j in range(3*i):
        pass
