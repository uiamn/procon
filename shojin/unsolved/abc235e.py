import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n

    def find(self, x: int) -> int:
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y) -> None:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return None
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def is_same(self, x, y) -> bool:
        return self.find(x) == self.find(y)


def kruskal(edges, n_v):
    """
        Kruskal 法により最小全域木を求める

        edges: 3 つ組からなるリスト
            (src_node, dst_node, weight)
            ただしノードの id は 1-based であるとする
        n_v: 頂点数

        tree_weight: 最小全域木の重さ
        tree: 最小全域木
    """

    edges.sort(key=lambda x: x[2])
    tree_weight = 0
    tree = []
    uf = UnionFind(n_v + 1)

    for src, dst, weight, qid in edges:
        if uf.is_same(src, dst):
            continue
        else:
            tree.append((src, dst, weight, qid))
            tree_weight += weight
            uf.unite(src, dst)

    return tree_weight, tree


N, M, Q = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c, 0))

queries = []

for i in range(Q):
    u, v, w = map(int, input().split())
    queries.append((u, v, w, i+1))

edges += queries

_, mst = kruskal(edges, N)
answer = [False for _ in range(Q+1)]

for _, _, _, qid in mst:
    answer[qid] = True

for i in range(1, Q+1):
    if answer[i]:
        print('Yes')
    else:
        print('No')
