N = int(input())
A = list(map(int, input().split()))

head = 0
tail = 0
ans = 0
tmp = A[0]

while head < N and tail < N:
    if tail == N-1 or tmp & A[tail + 1] != 0:
        n = tail - head + 1
        ans += n
        tmp ^= A[head]
        head += 1
    else:
        tmp |= A[tail + 1]
        tail += 1

print(ans)
