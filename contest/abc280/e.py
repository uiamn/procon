def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


N, P = map(int, input().split())
MOD = 998244353
P100 = modinv(100, MOD) * P % MOD

dp = [None for _ in range(N+1)]
dp[0] = 0

for i in range(1, N+1):
    if i == 1:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]*(((1-P100)) % MOD) + dp[i-2]*((P100) % MOD) + 1

    dp[i] %= MOD

print(dp[N])
