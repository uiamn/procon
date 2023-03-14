N, K = map(int, input().split())
P = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))


# ループするまで回してみる
one_loop_score = [0 for _ in range(N+1)]
one_loop_scores = [[] for _ in range(N+1)]

for init in range(1, N+1):
    is_visited = [False for _ in range(N+1)]
    now = init
    for _ in range(N):
        if is_visited[now]:
            break

        is_visited[now] = True
        next = P[now]
        one_loop_score[init] += C[next]
        one_loop_scores[init].append(one_loop_score[init])
        now = next

ans = -10 ** 9 - 1
for i in range(1, N+1):
    loopcount = len(one_loop_scores[i])

    if K <= loopcount:
        ans = max(ans, max(one_loop_scores[i][:K]))
    elif one_loop_score[i] <= 0:
        ans = max(ans, max(one_loop_scores[i]))
    elif K % loopcount == 0:
        ans = max(ans, (K//loopcount)*one_loop_score[i], (K//loopcount-1)*one_loop_score[i]+max(one_loop_scores[i]))
    else:
        ans = max(ans, max(0, max(one_loop_scores[i][:K%loopcount])) + (K//loopcount)*one_loop_score[i])

print(ans)
