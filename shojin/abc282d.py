import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n
        # self.val = [None for _ in range(n)]  # ノードに情報を付加したい場合

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
graph = [[] for _ in range(N+1)]
uf = UnionFind(N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    uf.unite(u, v)


for i in range(1, N+1):
    if uf.find(i) == i:
        is_visited = [None for _ in range(N+1)]
        q = [i]

        while q:
            n = q.pop()
            if is_visited[n]:
                continue

            is_visited[n] = True
            q += graph[n]

        # 二部グラフ判定をここに書く
        pass



