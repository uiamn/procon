H, W = map(int, input().split())
S = [input() for _ in range(H)]

a = lambda x, y: x*W+y
graph = [[] for _ in range(H*W)]

for i in range(H):
    for j in range(W):
        ijcolor = S[i][j]

        if i != 0:
            upcolor = S[i-1][j]
            if upcolor != ijcolor:
                graph[a(i, j)].append(a(i-1, j))
        if i != H-1:
            downcolor = S[i+1][j]
            if downcolor != ijcolor:
                graph[a(i, j)].append(a(i+1, j))
        if j != 0:
            leftcolor = S[i][j-1]
            if leftcolor != ijcolor:
                graph[a(i, j)].append(a(i, j-1))
        if j != W-1:
            rightcolor = S[i][j+1]
            if rightcolor != ijcolor:
                graph[a(i, j)].append(a(i, j+1))

is_visited = [False for _ in range(H*W)]
n_nodes_of_comps = []

ans = 0

for begin_node in range(H*W):
    if is_visited[begin_node]:
        continue

    is_visited[begin_node] = True
    tmp = 1
    next_nodes = [n for n in graph[begin_node]]
    n_while = 0
    n_black = 0

    if S[begin_node // W][begin_node % W] == '#':
        n_black += 1
    else:
        n_while += 1

    while next_nodes:
        n = next_nodes.pop()
        if is_visited[n]:
            continue

        if S[n // W][n % W] == '#':
            n_black += 1
        else:
            n_while += 1

        is_visited[n] = True
        next_nodes += graph[n]

    ans += n_while * n_black

print(ans)
