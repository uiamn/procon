N = int(input())

S = []
for i in range(N):
    for j, s in enumerate(input()):
        if s == '#':
            S.append((i, j))

T = []
for i in range(N):
    for j, t in enumerate(input()):
        if t == '#':
            T.append((i, j))

# 各回転ごとに左上を一致させるやうに平行移動して，全体が一致するかチェックする

def is_same(S, T):
    sorted_T = sorted(T, key=lambda x: x[0]*N+x[1])
    Stl = S[0]
    Ttl = sorted_T[0]
    d0, d1 = Stl[0] - Ttl[0], Stl[1] - Ttl[1]
    moved_T = [(t[0] + d0, t[1] + d1) for t in sorted_T]
    return S == moved_T

# そのまま
if is_same(S, T):
    print('Yes')
    exit(0)

# 時計回りに 90 度回転
T = [(t[1], N-t[0]) for t in T]
if is_same(S, T):
    print('Yes')
    exit(0)

# 時計回りに 90 度回転
T = [(t[1], N-t[0]) for t in T]
if is_same(S, T):
    print('Yes')
    exit(0)

# 時計回りに 90 度回転
T = [(t[1], N-t[0]) for t in T]
if is_same(S, T):
    print('Yes')
    exit(0)

print('No')
