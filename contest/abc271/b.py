N, Q = map(int, input().split())

a = [[]]

for _ in range(N):
    b = list(map(int, input().split()))
    a.append(b)


for _ in range(Q):
    s, t = map(int, input().split())

    print(a[s][t])

