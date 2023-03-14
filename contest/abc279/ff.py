import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int) -> None:
        self.root = {i: i for i in range(1, n+1)}
        self.rank = {i: 0 for i in range(1, n+1)}
        self.val = {i: i for i in range(1, n+1)}  # ノードに情報を付加したい場合

    def make(self, x: int, initval) -> int:
        self.root[x] = x
        self.rank[x] = 0
        self.val[x] = initval

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y) -> None:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return None
        else:
            self.root[y] = x

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
        uf.make(total+1, q[1])
        total += 1

        if uf.is_same(q[1], uf.val[q[1]]):
            uf.unite()

    else:
        print("ans",  uf.val[uf.find(q[1])])
