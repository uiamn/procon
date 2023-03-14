N, X = map(int, input().split())
# dp = [[j == 0 for j in range(X+1)] for _ in range(N)]  # dp[i][j] = 持ってゐる A_1, ..., A_{i+1} 円硬貨だけで j 円丁度支払へるか？

dp = [False for _ in range(X+1)]
dp[0] = True

for _ in range(N):
    A, B = map(int, input().split())
    next_dp = dp[:]

    for i, v in enumerate(dp):
        if v:
            for j in range(1, B+1):
                if i + j*A <= X:
                    next_dp[i+j*A] = True

    dp = next_dp

if dp[X]:
    print('Yes')
else:
    print('No')
