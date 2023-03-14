import sys
from typing import List, Tuple
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

N, M = map(int, input().split())
edges = []

for _ in range(M):
    edges.append(list(map(int, input().split())))

# 重みで辺集合を sort
edges.sort(key=lambda x: x[2])
uf = UnionFind(N+1)

i = 0
ans = 0
for src, dest, w in edges:
    if uf.is_same(src, dest):
        ans += max(w, 0)
    else:
        uf.unite(src, dest)

print(ans)
