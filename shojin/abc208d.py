import heapq
INF=2**64-1

def dijkstra(graph, src, INF=2**64-1):
    """
        頂点のインデクスは 1 から
        graph[i] = 頂点 i から出る辺のリスト 各要素は (行き先, 重さ) のタプル
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

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

dist = [None for _ in range(N+1)]

for i in range(1, N+1):
    dist[i] = dijkstra(graph, i)

val = [[0 for _ in range(N+1)] for _ in range(N+1)]

ans = 0

for k in range(1, N+1):
    for s in range(1, N+1):
        for t in range(1, N+1):
            if s == t:
                continue

            if dist[s][k] != INF and dist[k][t] != INF:
                if val[s][t] == 0:
                    val[s][t] = dist[s][k] + dist[k][t]
                else:
                    val[s][t] = min(val[s][t], dist[s][k] + dist[k][t])

    for v in val:
        ans += sum(v)

print(val)
print(dist)
print(ans)
