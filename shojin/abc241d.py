from bisect import bisect_left, insort

Q = int(input())
heap = []

queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))

for j in range(Q):
    q = queries[j]
    if q[0] == 1:
        insort(heap, q[1])
        # print(heap)
    else:
        c, x, k = q
        i = bisect_left(heap, x)
        # heap[0], heap[1], ..., heap[i] は x 以下の値
        # heap[i], ..., heap[N-1] は x 以上の値
        if c == 2:
            if i == len(heap) and k <= len(heap):
                print(heap[-k])
            elif i != len(heap) and i-k+1 >= 0:
                print(heap[i-k+1])
            else:
                print(-1)
        else:
            if i == 0 and k <= len(heap):
                print(heap[k-1])
            elif i != 0 and i+k-1 < len(heap):
                print(heap[i+k-1])
            else:
                print(-1)
