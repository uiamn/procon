from math import log2, floor

N, K = map(int, input().split())
A = list(map(int, input().split()))

X = 0

if K != 0:
    for i in range(floor(log2(K)) + 1):
        n_zero = 0
        n_one = 0

        for a in A:
            if (a >> i) & 1 == 0:
                n_zero += 1
            else:
                n_one += 1

        if n_zero > n_one:
            X += (1 << i)

if X > K:
    X -= (1 << (floor(log2(K)) + 1))


ans = 0
for a in A:
    ans += (a ^ X)

print(ans)
