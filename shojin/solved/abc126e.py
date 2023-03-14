import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int, n_components:int = None) -> None:
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n
        self.n_components = n_components if n_components is not None else n

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
            self.n_components -= 1
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.n_components -= 1

    def is_same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
uf = UnionFind(N+1, N)

for _ in range(M):
    X, Y, _ = map(int, input().split())
    uf.unite(X, Y)

print(uf.n_components)
