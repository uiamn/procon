import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n
        self.val = [0 for _ in range(n)]  # ノードに情報を付加したい場合

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
            self.val[x] += 1
            return None
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
            self.val[x] += self.val[y] + 1
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            self.val[y] += self.val[x] + 1
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def is_same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
uf = UnionFind(N+1)

for _ in range(M):
    u, v = map(int, input().split())
    uf.unite(u, v)

n_nodes = {}
for i in range(1, N+1):
    if uf.find(i) == i:
        n_nodes[i] = 0

for i in range(1, N+1):
    p = uf.find(i)
    n_nodes[p] += 1


for k, v in n_nodes.items():
    if v != uf.val[k]:
        print('No')
        exit(0)

print('Yes')
