import heapq

def dijkstra(graph, src, INF=2**64-1):
    """
        頂点のインデクスは 1 から
        graph[i] = 頂点 i から出る辺のリスト
        例 頂点 1 から 2 に重さ 3, 4 に重さ 5 の辺が生えてゐるとき
            graph[1] = [(2, 3), (4, 5)]
    """
    n = len(graph)
    dist = [INF for _ in range(n+1)]
    dist[src] = 0

    is_visited = [False for _ in range(n+1)]
    is_visited[src] = True

    heap = []
    for e in graph[src]:
        node_idx, weight = e
        heapq.heappush(heap, (weight, node_idx))

    while heap:
        weight, node_idx = heapq.heappop(heap)
        if is_visited[node_idx]:
            continue

        dist[node_idx] = weight
        is_visited[node_idx] = True

        for e in graph[node_idx]:
            if not is_visited[e[0]]:
                heapq.heappush(heap, (e[1] + dist[node_idx], e[0]))

    return dist


N, M, K = map(int, input().split())
graph = [[] for _ in range(2*N + 1)]
invv = lambda v: N + v

for _ in range(M):
    u, v, a = map(int, input().split())
    if u == v:
        continue

    if a == 1:
        graph[u].append((v, 1))
        graph[v].append((u, 1))
    else:
        graph[invv(u)].append((invv(v), 1))
        graph[invv(v)].append((invv(u), 1))

switchs = map(int, input().split())
for s in switchs:
    graph[s].append((invv(s), 0))
    graph[invv(s)].append((s, 0))

a = dijkstra(graph, 1)
ans = min(a[N], a[invv(N)])
if ans == 2**64-1:
    print(-1)
else:
    print(ans)
