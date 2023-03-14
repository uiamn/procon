import itertools

N, M = map(int, input().split())
S = []

for s in range(N):
    S.append(input())

# S_i で始まる T
start_s_ts = [[] for _ in range(N+1)]

for m in range(M):
    tm = input()
    for i, s in enumerate(S):
        if tm.startswith(s):
            start_s_ts[i].append(tm)
