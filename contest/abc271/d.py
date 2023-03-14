N, S = map(int, input().split())
a = []
b = []

for _ in range(N):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)


dp = [[None for __ in range(S+1)] for _ in range(N)]  # dp[i][j]: 1 から i+1 枚目のカードを使って総和を j にするやり方

if a[0] <= S:
    dp[0][a[0]] = 'H'
if b[0] <= S:
    dp[0][b[0]] = 'T'

for i in range(1, N):
    for j in range(1, S+1):
        if 0 <= j-a[i] <= S and dp[i-1][j-a[i]] is not None:
            dp[i][j] = dp[i-1][j-a[i]] + 'H'
        if 0 <= j-b[i] <= S and dp[i-1][j-b[i]] is not None:
            dp[i][j] = dp[i-1][j-b[i]] + 'T'

if dp[N-1][S] is not None:
    print('Yes')
    print(dp[N-1][S])
else:
    print('No')
