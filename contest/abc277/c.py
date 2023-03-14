N = int(input())
graph = {}

for _ in range(N):
    A, B = map(int, input().split())

    if A in graph:
        graph[A].append(B)
    else:
        graph[A] = [B]

    if B in graph:
        graph[B].append(A)
    else:
        graph[B] = [A]

is_visited = set([])
next_nodes = [1]
ans = 1

while next_nodes:
    n = next_nodes.pop()
    if n in is_visited:
        continue

    is_visited.add(n)

    if n in graph:
        next_nodes += graph[n]

    ans = max(ans, n)

print(ans)
