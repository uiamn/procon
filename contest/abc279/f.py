import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = {i: -1 for i in range(1, n+1)}
        self.rank = {i: 0 for i in range(1, n+1)}
        self.val = {i: i for i in range(1, n+1)}  # ノードに情報を付加したい場合

    def make(self, x: int):
        self.root[x] = -1
        self.rank[x] = 0

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


N, Q = map(int, input().split())

balls = {i: i for i in range(1, N+1)}
total = N

uf = UnionFind(N)

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        uf.unite(q[1], q[2])
    elif q[0] == 2:
        uf.make(total+1)
        uf.unite(q[1], total+1)
        total += 1
    else:
        print("ans",  uf.root[q[1]])
