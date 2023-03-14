from itertools import product
from bisect import bisect

N, T = map(int, input().split())
A = list(map(int, input().split()))

X = A[:N//2]
Y = A[N//2:]

Xcands = []
Ycands = []

for bits in product([0, 1], repeat=N//2):
    a = [x for bit, x in zip(bits, X) if bit == 1]
    Xcands.append(sum(a))

for bits in product([0, 1], repeat=(N-N//2)):
    a = [x for bit, x in zip(bits, Y) if bit == 1]
    Ycands.append(sum(a))

Xcands.sort()
Ycands.sort()
ans = 0

for cand in Xcands:
    if cand > T:
        break
    index = bisect(Ycands, T-cand)
    tmp = cand + Ycands[index-1]
    ans = max(tmp, ans)

print(ans)
