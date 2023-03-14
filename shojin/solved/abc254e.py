from copy import copy

N, M = map(int, input().split())
A = [set([i]) for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    A[a].add(b)
    A[b].add(a)

B = [set() for _ in range(N+1)]
C = [set() for _ in range(N+1)]

for i in range(1, N+1):
    Bi = copy(A[i])
    for j in A[i]:
        Bi |= A[j]

    B[i] = Bi

for i in range(1, N+1):
    Ci = copy(B[i])
    for j in B[i]:
        Ci |= A[j]

    C[i] = Ci

Q = int(input())

ans = []

for _ in range(Q):
    x, k = map(int, input().split())
    if k == 0:
        ans.append(x)
    elif k == 1:
        ans.append(sum(A[x]))
    elif k == 2:
        ans.append(sum(B[x]))
    elif k == 3:
        ans.append(sum(C[x]))

for a in ans:
    print(a)
