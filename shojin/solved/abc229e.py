import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n
        self.members = n

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
            self.members -= 1
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.members -= 1

    def is_same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = [None for _ in range(N+1)]  # ans[i] = 頂点 i まで消したときにいくつの連結成分に分かれてゐるか

uf = UnionFind(N+1)
for i in range(N, 0, -1):
    ans[i] = uf.members - i - 1
    for c in graph[i]:
        uf.unite(i, c)

for i in range(1, N+1):
    print(ans[i])
