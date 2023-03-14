N, C = map(int, input().split())
queries = []

for _ in range(N):
    T, A = map(int, input().split())
    queries.append((T, A))

X = [[None for _ in range(N)] for _ in range(2)]  # X[b][i] = b に対して操作 1, ..., i+1 を繰り返し行ったもの

b0 = 0
b1 = 2**30 - 1

for i, (t, a) in enumerate(queries):
    if t == 1:
        b0 &= a
        b1 &= a
    elif t == 2:
        b0 |= a
        b1 |= a
    else:
        b0 ^= a
        b1 ^= a

    X[0][i] = b0
    X[1][i] = b1

for i, (t, a) in enumerate(queries):
    ans = 0
    for k in range(30):
        if (C >> k) & 1 == 0:
            ans |= (((X[0][i] >> k) & 1) << k)
        else:
            ans |= (((X[1][i] >> k) & 1) << k)

    print(ans)
    C = ans
