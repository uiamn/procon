from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def is_crossing(c1, c2):
    d2 = (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2
    r1 = max(c1[2], c2[2])
    r2 = min(c1[2], c2[2])
    rr1 = (r1-r2)**2
    rr2 = (r1+r2)**2

    return rr1 <= d2 and d2 <= rr2

N = int(input())
sx, sy, tx, ty = map(int, input().split())
circles = []

for _ in range(N):
    circles.append(list(map(int, input().split())))

circles.append([sx, sy, 0])
circles.append([tx, ty, 0])

M = N + 2
uf = UnionFind(M)

for i in range(M-1):
    for j in range(i+1, M):
        if is_crossing(circles[i], circles[j]):
            uf.union(i, j)

if uf.same(N, N+1):
    print('Yes')
else:
    print('No')
