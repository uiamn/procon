N, Q = map(int, input().split())
res = [0 for _ in range(N+1)]

for _ in range(Q):
    c, x = map(int, input().split())

    if c == 1:
        res[x] += 1
    elif c == 2:
        res[x] += 2
    else:
        if res[x] >= 2:
            print('Yes')
        else:
            print('No')
