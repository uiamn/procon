from bisect import bisect, bisect_left

H, W = map(int, input().split())
A = []

for _ in range(H):
    A.append(list(map(int, input().split())))

# 列の最大値順にソート
A.sort(key=lambda x: max(x))

row_sorted_A = []

# 各行もソート
for a in A:
    row_sorted_A.append(sorted(a))

for i in range(H-1):
    if A[i][-1] > min([H*W+1] + [x for x in A[i+1] if x != 0]):
        print('No')
        exit(0)


for a in A:
    n_0 = bisect(row_sorted_A, 0)

    for x in a:
        if x == 0:
            continue

        l = bisect_left()

