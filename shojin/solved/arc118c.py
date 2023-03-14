N = int(input())
A = []

if N == 3:
    print('6 10 15')
    exit(0)


for i in range(6, 10001):
    if (i % 6 == 0) or (i % 10 == 0) or (i % 15 == 0):
        A.append(i)

        if len(A) == N:
            break

print(' '.join(list(map(str, A))))
