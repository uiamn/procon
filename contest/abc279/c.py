H, W = map(int, input().split())
Ss = [input() for _ in range(H)]
Ts = [input() for _ in range(H)]

scols = [[Ss[i][w] for i in range(H)] for w in range(W)]
tcols = [[Ts[i][w] for i in range(H)] for w in range(W)]

scols.sort()
tcols.sort()

if scols == tcols:
    print('Yes')
else:
    print('No')
