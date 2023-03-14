X, K = map(int, input().split())

for i in range(1, K+1):
    X = round(X+1, -i)

print(X)
