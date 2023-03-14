import copy
H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

rows = [set([b for b in a if b is not None]) for a in A]
cols = []

for i in range(W):
    s = set()
    for j in range(H):
        s.add(A[j][i])

    cols.append(s)

rowstmp = [set()]
rowstmpinv = [set()]
colstmp = [set()]
colstmpinv = [set()]

tmp = set()
for i in range(W-w+1):
    tmp |= cols[i]
    colstmp.append(copy.copy(tmp))

tmp = set()
for i in range(W-1, w-1, -1):
    tmp |= cols[i]
    colstmpinv.append(copy.copy(tmp))

tmp = set()
for i in range(H-h+1):
    tmp |= rows[i]
    rowstmp.append(copy.copy(tmp))

tmp = set()
for i in range(H-1, h-1, -1):
    tmp |= rows[i]
    rowstmpinv.append(copy.copy(tmp))

rowstmp.append(set())
rowstmpinv.append(set())
colstmp.append(set())
colstmpinv.append(set())

# print(rowstmp)
# print(rowstmpinv)
# print(colstmp)
# print(colstmpinv)

for k in range(H-h+1):
    for l in range(W-w+1):
        ansset = rowstmp[k] | rowstmpinv[H-k-h] | colstmp[l] | colstmpinv[W-l-w]

        # print(ansset)
        # print(len(ansset))
        print(len(ansset), end='')
        if l == W-w:
            print()
        else:
            print(' ', end='')
