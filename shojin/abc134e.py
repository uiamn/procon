import heapq

N = int(input())
A = [int(input()) for _ in range(N)]

# head = 1
# tail = 10 ** 5
# pivot = (tail + head) // 2

print(A)
heap = [A[0]]

for i in range(1, N):
    if A[i] > heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, A[i])
    else:
        heapq.heappush(heap, A[i])

print(len(heap))
