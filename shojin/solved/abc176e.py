from itertools import product

H, W, M = map(int, input().split())
targets = []
target_hashs = set()

for _ in range(M):
    h, w = map(int, input().split())
    targets.append((h, w))
    target_hashs.add(h*W + w)

row_count = [0 for _ in range(H+1)]
col_count = [0 for _ in range(W+1)]

for h, w in targets:
    row_count[h] += 1
    col_count[w] += 1

row_max = 0
row_max_idx_cand = []
col_max = 0
col_max_idx_cand = []

for i in range(1, H+1):
    r = row_count[i]
    if row_max < r:
        row_max = r
        row_max_idx_cand = [i]
    elif row_max == r:
        row_max_idx_cand.append(i)

for i in range(1, W+1):
    c = col_count[i]
    if col_max < c:
        col_max = c
        col_max_idx_cand = [i]
    elif col_max == c:
        col_max_idx_cand.append(i)

if len(row_max_idx_cand) * len(col_max_idx_cand) > M:
    print(row_max + col_max)
    exit(0)

for r, c in product(row_max_idx_cand, col_max_idx_cand):
    if (r*W + c) not in target_hashs:
        print(row_max + col_max)
        exit(0)

print(row_max + col_max - 1)
