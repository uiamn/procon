H, W = map(int, input().split())
black_sq_u = []
black_sq_v = []

for x in range(1, H+1):
    row = input()

    for i, c in enumerate(row):
        if c == '#':
            y = i+1
            u = x + y
            v = x - y
            black_sq_u.append(u)
            black_sq_v.append(v)

black_sq_u.sort()
black_sq_v.sort()
ans = 0

print(black_sq_u)
print(black_sq_v)

if len(black_sq_u) != 1:
    for i in range(len(black_sq_u)-1):
        ans = max((black_sq_u[i] - black_sq_u[i+1]) // 2, ans)
        ans = max((black_sq_v[i] - black_sq_v[i+1]) // 2, ans)
else:
    u = black_sq_u[0]
    v = black_sq_v[0]
    ans = max(abs(u-2), abs(u-H-W), abs(v - (1-W)), abs(v - (H-1)))

print(ans)
