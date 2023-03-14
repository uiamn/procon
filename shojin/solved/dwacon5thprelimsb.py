N, K = map(int, input().split())
A = list(map(int, input().split()))
Asum = []
tmpsum = 0
for a in A:
    tmpsum += a
    Asum.append(tmpsum)

candidates = []

for i in range(N):
    for j in range(i, N):
        if i != 0:
            b = Asum[j] - Asum[i-1]
        else:
            b = Asum[j]

        candidates.append(b)

ans = 0

for i in range(40, -1, -1):
    cnt = 0
    next_cand = []

    for cand in candidates:
        if (cand >> i) & 1 == 1:
            cnt += 1
            next_cand.append(cand)

    if cnt >= K:
        candidates = next_cand
        ans += (1 << i)

print(ans)
