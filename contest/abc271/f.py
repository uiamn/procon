import bisect


def xors(srcx, srcy, destx, desty, grid):
    # (srcx, srcy) から (destx, desty) に移動する全ての方法について，通るマスの排他的論理和を求める関数．
    if srcx == destx and srcy == desty:
        return [grid[srcx][srcy]]

    result = []
    if srcx < destx:
        result += [x^grid[destx][desty] for x in xors(srcx, srcy, destx-1, desty, grid)]

    if srcy < desty:
        result += [x^grid[destx][desty] for x in xors(srcx, srcy, destx, desty-1, grid)]

    return result


N = int(input())
grid = [[]]

for _ in range(N):
    grid.append([None] + list(map(int, input().split())))

P = []  # P[i-1] = マス (1,1) から マス (i, N+1-i) に移動する全ての方法について，通るマスの排他的論理和たち
Q = []  # Q[i-1] = マス (i, N+1-i) から マス (N, N) に移動する全ての方法について，通るマスの排他的論理和たち

for i in range(N):
    P.append(xors(1, 1, i+1, N-i, grid))
    Q.append(sorted(xors(i+1, N-i, N, N, grid)))

result = 0
for i, (pp, qq) in enumerate(zip(P, Q)):
    for p in pp:
        l = bisect.bisect_left(qq, p^grid[i+1][N-i])
        r = bisect.bisect_right(qq, p^grid[i+1][N-i])

        result += (r-l)

print(result)
