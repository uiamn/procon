import heapq

N, M = map(int, input().split())
tasks = []  # かかる日数を昇順に並べたヒープ

for i in range(N):
    A, B = map(int, input().split())
    heapq.heappush(tasks, (A, B))

cands = []
ans = 0

for i in range(1, M+1):
    while tasks and tasks[0][0] <= i:
        a, b = heapq.heappop(tasks)
        heapq.heappush(cands, -b)

    if len(cands):
        ans -= heapq.heappop(cands)


print(ans)
