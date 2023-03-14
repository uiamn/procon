N, M = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    print(0)
    exit(0)

A.sort()
A += A

removable = []
i = 0
while i < N:
    j = 0
    while j < N:
        if A[i+j] == A[i+j+1] or (A[i+j] + 1) % M == A[i+j+1]:
            j += 1
        else:
            break

    removable.append([i, i+j])
    i += j + 1

csum = [0]
csumtmp = 0
for a in A[:N]:
    csumtmp += a
    csum.append(csumtmp)

Asum = csumtmp

ans = -1
for remove in removable:
    l, r = remove

    if r < N:
        ans = max(ans, csum[r+1] - csum[l])
    elif l < N:
        ans = max(ans, csum[r % N + 1] + (csum[N] - csum[l]))

print(max((Asum - ans), 0))
