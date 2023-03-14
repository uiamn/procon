from collections import deque

H, W = map(int, input().split())
A = [input() for _ in range(H)]
teleporter = {chr(i): [] for i in range(97, 122+1)}

s = None
g = None

for i in range(H):
    for j in range(W):
        if 97 <= ord(A[i][j]) <= 122:
            teleporter[A[i][j]].append(i*W+j)
        elif A[i][j] == 'S':
            s = i*W+j
        elif A[i][j] == 'G':
            g = i*W+j

is_visited = [False for _ in range(H*W)]
candidate = deque([(0, s)])

c2i = lambda y, x: y*W+x

while candidate:
    node = candidate.popleft()
    node_dist, node_idx = node

    if is_visited[node_idx]:
        continue

    if node_idx == g:
        print(node_dist)
        exit(0)

    node_x = node_idx % W
    node_y = node_idx // W

    is_visited[node_idx] = True

    if len(candidate) >= 1:
        fdist = candidate[0][0]
    else:
        fdist = 0

    if node_x != 0 and not is_visited[node_idx-1] and A[node_y][node_x-1] != '#':
        if fdist == node_dist + 1:
            candidate.appendleft((node_dist+1, node_idx-1))
        else:
            candidate.append((node_dist+1, node_idx-1))
    if node_x != W-1 and not is_visited[node_idx+1] and A[node_y][node_x+1] != '#':
        if fdist == node_dist + 1:
            candidate.appendleft((node_dist+1, node_idx+1))
        else:
            candidate.append((node_dist+1, node_idx+1))
    if node_y != 0 and not is_visited[node_idx-W] and A[node_y-1][node_x] != '#':
        if fdist == node_dist + 1:
            candidate.appendleft((node_dist+1, node_idx-W))
        else:
            candidate.append((node_dist+1, node_idx-W))
    if node_y != H-1 and not is_visited[node_idx+W] and A[node_y+1][node_x] != '#':
        if fdist == node_dist + 1:
            candidate.appendleft((node_dist+1, node_idx+W))
        else:
            candidate.append((node_dist+1, node_idx+W))


    if 97 <= ord(A[node_y][node_x]) <= 122:
        for t in teleporter[A[node_y][node_x]]:
            if is_visited[t]:
                continue

            if fdist == node_dist + 1:
                candidate.appendleft(((node_dist+1, t)))
            else:
                candidate.append(((node_dist+1, t)))

        # teleporter を 2 度使ふことはないはず．
        teleporter[A[node_y][node_x]] = []

print(-1)
