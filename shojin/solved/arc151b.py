import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n
        self.n_components = n

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
P = list(map(lambda x: int(x)-1, input().split()))
MOD = 998244353
uf = UnionFind(N)

ans = 0

for i, p in enumerate(P):
    if uf.is_same(i, p):
        continue

    if uf.n_components > 2:
        ans += pow(M, uf.n_components-2, MOD) * (M*(M-1)) // 2
        ans %= MOD
    else:  # n_components == 2
        ans += (M*(M-1)) // 2
        ans %= MOD

    uf.unite(i, p)

print(ans)
