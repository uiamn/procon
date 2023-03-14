from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]
edges = []

for _ in range(N-1):
    a, b = map(int, input().split())
    edges.append((a, b))
    tree[a].append(b)
    tree[b].append(a)

c = list(map(int, input().split()))
c.sort(reverse=True)

stack = deque()
stack.append(1)

is_visited = [False for _ in range(N+1)]
d = [None for _ in range(N+1)]

while stack:
    n = stack[-1]
    is_visited[n] = True

    flag = True
    # n の隣接頂点が全て探索済みなら値を決定
    for ne in tree[n]:
        if not is_visited[ne]:
            stack.append(ne)
            flag = False

    if flag:
        d[n] = c.pop()
        stack.pop()

ans = 0
for e in edges:
    a, b = e
    ans += min(d[a], d[b])

print(ans)
print(' '.join(map(str, d[1:])))
