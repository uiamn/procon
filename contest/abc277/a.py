N, X = map(int, input().split())
P = list(map(int, input().split()))

for k in range(N):
    if P[k] == X:
        print(k+1)
        exit(0)
