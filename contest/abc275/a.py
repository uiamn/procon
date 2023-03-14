N = int(input())
H = list(map(int, input().split()))

ans = 0
maxh = -1
for i in range(N):
    if maxh < H[i]:
        maxh = H[i]
        ans = i

print(ans + 1)
