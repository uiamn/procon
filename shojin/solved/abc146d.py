N = int(input())
tree = [[] for _ in range(N+1)]
edge_index = {}

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    edge_index[(a, b)] = i

# 最大次数を持つ頂点を探す
max_d = 0
max_d_v = None
for v, children in enumerate(tree):
    if max_d < len(children):
        max_d = len(children)
        max_d_v = v

is_visited = [False for _ in range(N+1)]
is_visited[max_d_v] = True
queue = []
colors = [0 for _ in range(N-1)]

for i, c in enumerate(tree[max_d_v]):
    queue.append((c, i+1))
    colors[edge_index[min(max_d_v, c), max(max_d_v, c)]] = i+1

while queue:
    v, color = queue.pop()
    is_visited[v] = True

    ii = 0

    for c in tree[v]:
        if is_visited[c]:
            continue

        ii += 1
        if ii == color:
            ii += 1

        queue.append((c, ii))
        colors[edge_index[min(v, c), max(v, c)]] = ii

print(max_d)
for c in colors:
    print(c)
