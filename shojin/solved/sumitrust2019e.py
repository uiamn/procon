MOD = 1000000007
N = int(input())
A = list(map(int, input().split()))

X = [0, 0, 0]
ans = 1

for a in A:
    ans *= sum([x == a for x in X])
    ans %= MOD
    for i in range(3):
        if X[i] == a:
            X[i] += 1
            break

print(ans)
