N, X = map(int, input().split())
A = list(map(int, input().split()))

first_minus_1_index = None

for i, a in enumerate(A):
    if a == -1:
        first_minus_1_index = i
        break
else:
    xor = 0
    for a in A:
        xor ^= a

    if xor == X:
        print(' '.join(map(str, A)))
    else:
        print('-1')

    exit(0)

xor = 0
for a in A:
    if a == -1:
        pass
    else:
        xor ^= a

if X ^ xor > X:
    print(-1)
    exit(0)

A[first_minus_1_index] = X ^ xor

for a in A[:-1]:
    print(a if a != -1 else 0, end=' ')

print(A[-1] if A[-1] != -1 else 0)
