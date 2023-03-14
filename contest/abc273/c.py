from bisect import bisect


N = int(input())
A = list(map(int, input().split()))
sortedA = sorted(list(set(A)))
M = len(sortedA)

ans = [0 for _ in range(N)]


for i in range(N):
    ans[M - bisect(sortedA, A[i])] += 1

for a in ans:
    print(a)
