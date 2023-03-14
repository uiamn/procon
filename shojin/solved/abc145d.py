MOD = 10 ** 9 + 7

factorial = [1]
v = 1
for i in range(1, 2*10**6+1):
    v *= i
    v %= MOD
    factorial.append(v)

factorial_inv = [None for _ in range(10**6+1)] ## factorial_inv[i] = (i!)^{-1}
v = pow(factorial[10**6], MOD-2, MOD)
factorial_inv[10**6] = v

for i in range(1, 10**6+1):
    n = 10**6 - i
    v *= (n+1)
    v %= MOD
    factorial_inv[n] = v

X, Y = map(int, input().split())

if (2*X-Y) % 3 != 0 or (2*Y-X) % 3 != 0:
    print(0)
    exit(0)

m = (2*X-Y) // 3
n = (2*Y-X) // 3

if m < 0 or n < 0:
    print(0)
    exit(0)

print((factorial[m+n] * factorial_inv[n] * factorial_inv[m]) % MOD)


