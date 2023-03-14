H, N = map(int, input().split())

magic = []
max_attack = -1

for _ in range(N):
    m = list(map(int, input().split()))
    magic.append(m)
    max_attack = max(max_attack, m[0])

dp = [None for _ in range(H+max_attack+1)]
dp[0] = 0

for h in range(1, H+max_attack+1):
    val = 10 ** 9
    for i in range(N):
        m = magic[i]
        if h - m[0] >= 0:
            val = min(val, dp[h-m[0]] + m[1])

    dp[h] = val

ans = 10 ** 9
for h in range(H, H+max_attack+1):
    ans = min(ans, dp[h])

print(ans)
