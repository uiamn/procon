from itertools import combinations

N, K = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

if K == 1:
    print('Infinity')
    exit(0)

already_checked = [[False for _ in range(N)] for __ in range(N)]

ans = 0

for i in range(N-2):
    xi, yi = points[i]
    for j in range(i+1, N-1):
        if already_checked[i][j]:
            continue

        xj, yj = points[j]
        n_onsameline = 0
        is_onsameline = lambda x, y: (xi-xj)*(y-yi) == (yi-yj)*(x-xi)
        onsamelinepoints = [i, j]

        for k in range(j+1, N):
            if is_onsameline(*points[k]):
                n_onsameline += 1
                onsamelinepoints.append(k)
                print(xi, yi, xj, yj, *points[k], i, j, k)

        for k1, k2 in combinations(onsamelinepoints, 2):
            already_checked[k1][k2] = True

        if n_onsameline >= K-2:
            print(xi, yi, xj, yj)
            ans += 1

print(already_checked)
print(ans)
