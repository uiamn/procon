N = int(input())

tree = [{} for _ in range(N+1)]
color = [None for _ in range(N+1)]

for _ in range(N-1):
    u, v, w = map(int, input().split())
    tree[u][v] = w
    tree[v][u] = w

color[1] = 0
cand = []  # 候補ノードと直前ノードのタプル
is_visited = [False for _ in range(N+1)]
is_visited[1] = True

for n in tree[1].keys():
    cand.append((n, 1))

while cand:
    n, prev_n = cand.pop()
    if is_visited[n]:
        continue

    is_visited[n] = True
    color[n] = color[prev_n] if tree[prev_n][n] % 2 == 0 else (1^color[prev_n])

    for next in tree[n].keys():
        cand.append((next, n))

for i in range(1, N+1):
    print(color[i])
