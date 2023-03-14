import collections

N, X, Y = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

is_visited = [False for _ in range(N+1)]
candidate = collections.deque([[X]])

while candidate:
    path = candidate.popleft()
    node = path[-1]

    if is_visited[node]:
        continue

    is_visited[node] = True
    neighbors = graph[node]

    for n in neighbors:
        if n == Y:
            print(' '.join(list(map(str, path + [n]))))
            exit(0)
        if not is_visited[n]:
            candidate.append(path + [n])
