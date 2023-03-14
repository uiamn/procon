import math

N = int(input())
A = list(map(int, input().split()))

l = A[0]
r = A[-1]
L = [None for _ in range(N)]  # L[i] = gcd( A[0], ..., A[i] )
R = [None for _ in range(N)]  # R[i] = gcd( A[i], ..., A[N-1])
L[0] = l
R[N-1] = r

for i in range(1, N):
    l = math.gcd(l, A[i])
    L[i] = l

for i in range(N-2, -1, -1):
    r = math.gcd(r, A[i])
    R[i] = r

ans = 1
for i in range(1, N-1):
    ans = max(ans, math.gcd(L[i-1], R[i+1]))

print(max(ans, L[N-2], R[1]))
