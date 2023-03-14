from bisect import bisect

N, M = map(int, input().split())
h = [0] + sorted(list(map(int, input().split())))
W = map(int, input().split())

if N == 1:
    ans = 10 ** 18
    for w in W:
        ans = min(ans, abs(h[1] - w))

    print(ans)
    exit(0)

X = [0 for _ in range((N-1)//2 + 1)]
Y = [0 for _ in range((N-1)//2 + 1)]

X[1] = h[3] - h[2]
Y[1] = h[2] - h[1]

for i in range(2, (N-1)//2 + 1):
    X[i] = X[i-1] + h[2*i+1] - h[2*i]
    Y[i] = Y[i-1] + h[2*i] - h[2*i-1]

org = X[-1]
ans = 10 ** 18

for w in W:
    j = bisect(h, w)
    if j % 2 == 0:
        tmp = org - X[j // 2 - 1] + w - h[j-1] + Y[j // 2 - 1]
        ans = min(ans, tmp)
    else:
        tmp = org - X[(j-1) // 2] + h[j] - w + Y[(j-1) // 2]
        ans = min(ans, tmp)

print(ans)
