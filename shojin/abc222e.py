N, M, K = map(int, input().split())
A = list(map(int, input().split()))

tree = [[] for _ in range(N+1)]

for i in range(N-1):
    u, v = map(int, input().split())
    tree[u].append((v, i))
    tree[v].append((u, i))

edge_count = [0 for _ in range(N-1)]

for i in range(M-1):
    src = A[i]
    dst = A[i+1]

    is_visited = [False for _ in range(N+1)]
    cands = [(src, [])]
    result_path = None

    while cands:
        n, path = cands.pop()
        if is_visited[n]:
            continue

        is_visited[n] = True
        if n == dst:
            result_path = path
            break

        cands += [(nn, path + [idx]) for nn, idx in tree[n] if not is_visited[nn]]

    for e in result_path:
        edge_count[e] += 1

S = sum(edge_count)

if S - K < 0:
    print(0)
    exit(0)

if (S-K) % 2 != 0:
    print(0)
    exit(0)

MOD = 998244353

nonzero_edge_count = sorted(list(filter(lambda x: x != 0, edge_count)))
n_zero_count = N - 1 - len(nonzero_edge_count)

if len(nonzero_edge_count) == 0:
    if K == 0:
        print(pow(2, n_zero_count, MOD))
    else:
        print(0)
    exit(0)

dp = [0 for _ in range((S-K) // 2 + 1)]  # dp[i][j] = 0 から i までで和が j となるやうなものの数

if nonzero_edge_count[0] > (S-K) // 2:
    print(0)
    exit(0)

dp[nonzero_edge_count[0]] = 1

for i in range(1, len(nonzero_edge_count)):
    nextdp = [dp[i] for i in range((S-K) // 2 + 1)]
    for j in range(nonzero_edge_count[i], (S-K) // 2 + 1):
        nextdp[j] += dp[j-nonzero_edge_count[i]]

    nextdp[nonzero_edge_count[i]] += 1
    dp = nextdp

print((pow(2, n_zero_count, MOD) * dp[(S-K) // 2]) % MOD)
