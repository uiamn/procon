N = int(input())
S = list(map(int, input().split()))

A = [S[0]]

for i in range(1, len(S)):
    A.append(S[i] - S[i-1])

print(' '.join(map(str, A)))
