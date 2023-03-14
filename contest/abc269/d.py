import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n
        self.is_red = [False for _ in range(n)]

    def find(self, x: int) -> int:
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def n_red_roots(self):
        return len([i for i, x in enumerate(self.root) if x < 0 and self.is_red[i]])


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

    def same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

N = int(input())
PAD = 2001
uf = UnionFind(PAD*PAD)
c2i = lambda x, y: x + y*PAD

for _ in range(N):
    X, Y = map(int, input().split())
    X += 1000
    Y += 1000

    uf.is_red[c2i(X, Y)] = True

    if X != 0 and Y != 0 and uf.is_red[c2i(X-1, Y-1)]:
        uf.unite(c2i(X, Y), c2i(X-1, Y-1))
    if X != 0 and uf.is_red[c2i(X-1, Y)]:
        uf.unite(c2i(X, Y), c2i(X-1, Y))
    if Y != 0 and uf.is_red[c2i(X, Y-1)]:
        uf.unite(c2i(X, Y), c2i(X, Y-1))
    if Y != 2000 and uf.is_red[c2i(X, Y+1)]:
        uf.unite(c2i(X, Y), c2i(X, Y+1))
    if X != 2000 and uf.is_red[c2i(X+1, Y)]:
        uf.unite(c2i(X, Y), c2i(X+1, Y))
    if X != 2000 and Y != 2000 and uf.is_red[c2i(X+1, Y+1)]:
        uf.unite(c2i(X, Y), c2i(X+1, Y+1))

print(uf.n_red_roots())

