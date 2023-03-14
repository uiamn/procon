H, W = map(int, input().split())
ans = 0

for _ in range(H):
    s = input()

    for c in s:
        if c == '#':
            ans += 1

print(ans)
