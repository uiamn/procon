H, W = map(int, input().split())
A = [''] + [list(map(lambda x: 1 if x=='+' else -1, ' ' + input())) for _ in range(H)]

# dp[i][j] = i, j から H, W に最適に移動するときに高橋くんが得る点数 - 青木くんが得る点数
dp = [[None for _ in range(W+1)] for _ in range(H+1)]
dp[H][W] = 0

for i in range(W-1, 0, -1):
    if (H+i) % 2 == 0:
        dp[H][i] = dp[H][i+1] + A[H][i+1]
    else:
        dp[H][i] = dp[H][i+1] - A[H][i+1]

for i in range(H-1, 0, -1):
    if (W+i) % 2 == 0:
        dp[i][W] = dp[i+1][W] + A[i+1][W]
    else:
        dp[i][W] = dp[i+1][W] - A[i+1][W]

# i+j が偶数になるマス (i, j) から動かす人 = 高橋くん
for i in range(H-1, 0, -1):
    for j in range(W-1, 0, -1):
        if (i+j) % 2 == 0:
            dp[i][j] = max(dp[i+1][j] + A[i+1][j], dp[i][j+1] + A[i][j+1])
        else:
            dp[i][j] = min(dp[i+1][j] - A[i+1][j], dp[i][j+1] - A[i][j+1])

if dp[1][1] > 0:
    print('Takahashi')
elif dp[1][1] < 0:
    print('Aoki')
else:
    print('Draw')
