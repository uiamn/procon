import heapq
from typing import List

class ToNode:
    def __init__(self, to: int, cost: int) -> None:
        self.to = to
        self.cost = cost

def dijkstra(n_nodes: int, adj: List[ToNode], begin: int, end: int, INF: int = 2**64-1):
    class Node:
        def __init__(self, index, min_cost) -> None:
            self.index = index
            self.min_cost = min_cost

        def __lt__(self, other) -> bool:
            return self.min_cost < other.min_cost

    q = []
    begin_node = Node(begin, 0)
    heapq.heappush(q, begin_node)
    min_cost = [INF for _ in range(n_nodes+1)]

    while len(q) != 0:
        node = heapq.heappop(q)

        if min_cost[node.index] != INF:
            continue

        min_cost[node.index] = node.min_cost

        for to_node in adj[node.index]:
            new_node = Node(to_node.to, node.min_cost + to_node.cost)
            heapq.heappush(q, new_node)


    return min_cost[end]

N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]
edges = [None]

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append([A, B, C])
    graph[A].append(ToNode(B, C))

E = list(map(int, input().split()))

lastdest = 1
res = 0

for e in E:
    src, dest, cost = edges[e]
    print(edges[e])
    po = dijkstra(N, graph, lastdest, src)
    print(po)
    res += po
    res += cost
    lastdest = dest

res += dijkstra(N, graph, lastdest, N)

print(res)
