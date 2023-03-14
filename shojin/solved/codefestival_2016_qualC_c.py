MOD = 10**9 + 7
N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

if T[-1] != A[0]:
    print(0)
    exit(0)


l = [1 for _ in range(N)]
r = [min(T[i], A[i]) for i in range(N)]

l[0] = T[0]

for i in range(1, N):
    if T[i-1] < T[i]:
        l[i] = T[i]

if r[-1] < A[-1]:
    print(0)
    exit(0)

r[-1] = A[-1]
l[-1] = A[-1]

for i in range(N-1-1, -1, -1):
    if A[i+1] < A[i]:
        if A[i] < l[i] or r[i] < A[i]:
            print(0)
            exit(0)
        l[i] = A[i]
        r[i] = A[i]

ans = 1
for ll, rr in zip(l, r):
    ans *= (rr - ll + 1)
    ans %= MOD

print(ans)
