# varidated: https://atcoder.jp/contests/typical90/tasks/typical90_m
import heapq

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
