N = int(input())
p = list(map(int, input().split()))
x = [None for _ in range(N)]

for i in range(N):
    x[p[i]] = (p[i] - i) % N

initial_fuman = 0
for a in x:
    initial_fuman += a if a <= N / 2 else N - a

S = [0 for _ in range(N)]

for i in range(N):
    j = x[i]
    if j >= N / 2:
        print(j, j-(N//2), j+1)
        S[j-(N//2)] += 1
        if j != N-1:
            S[j+1] -= 1
    else:
        print(j, j+1, (j-(N//2))%N)
        S[0] += 1
        S[j+1] -= 1
        S[(j-(N//2))%N] += 1

ssum = [S[0]]
tmpsum = S[0]
for i in range(1, N):
    tmpsum += S[i]
    ssum.append(tmpsum)

maxarg = ssum.index(max(ssum)) + 1

y = [None for _ in range(N)]
for i in range(N):
    y[p[(i-maxarg) % N]] = (p[(i-maxarg) % N] - i) % N
fuman = 0
for a in y:
    fuman += a if a <= N / 2 else N - a

print(fuman)

print(x)
print(S)
print(ssum)
print(initial_fuman - max(ssum))

