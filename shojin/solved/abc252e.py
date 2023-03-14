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

    prev_node = [None for _ in range(n+1)]

    heap = []
    for e in graph[src]:
        node_idx, weight = e
        heapq.heappush(heap, (weight, node_idx, src))

    while heap:
        weight, node_idx, prev = heapq.heappop(heap)
        if is_visited[node_idx]:
            continue

        dist[node_idx] = weight
        is_visited[node_idx] = True
        prev_node[node_idx] = prev

        for e in graph[node_idx]:
            if not is_visited[e[0]]:
                heapq.heappush(heap, (e[1] + dist[node_idx], e[0], node_idx))

    return prev_node

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
edge_index = {}
for i in range(1, M+1):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

    if min(A, B) in edge_index:
        edge_index[min(A, B)][max(A, B)] = i
    else:
        edge_index[min(A, B)] = {max(A, B): i}

prev_node = dijkstra(graph, 1)
ans = []

for i in range(2, N+1):
    prev = prev_node[i]
    ans.append(edge_index[min(i, prev)][max(i, prev)])

print(' '.join(map(str, ans)))
