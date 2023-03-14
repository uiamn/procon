N = int(input())
A = list(map(int, input().split()))

tmp = [0 for _ in range(60)]

for i in range(60):
    count_1 = 0
    for a in A:
        if (a >> i) & 1:
            count_1 += 1

    tmp[i] = (count_1) * (N - count_1)

MOD = 10**9 + 7
ans = 0

for i, v in enumerate(tmp):
    ans += (v * pow(2, i, MOD)) % MOD
    ans %= MOD

print(ans)
