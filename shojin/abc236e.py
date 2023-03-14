# 人は 0, 1, ..., 2N-1 とする
N = int(input())
A = []

for i in range(2*N - 1):
    A.append([None for _ in range(i+1)] + list(map(int, input().split())))

print(A)

current_pairs = []
current_fun = 0

for i in range(N):
    next_pairs = current_pairs + [(2*i, 2*i+1)]
    tmp_fun = current_fun ^ A[2*i][2*i+1]

    for ii, pair in enumerate(current_pairs):
        j, k = pair
        fun1 = current_fun ^ A[j][k] ^ A[j][2*i] ^ A[k][2*i+1]
        fun2 = current_fun ^ A[j][k] ^ A[k][2*i] ^ A[j][2*i+1]

        if tmp_fun < fun1:
            next_pairs = current_pairs[:ii] + current_pairs[ii+1:] + [(j, 2*i), (k, 2*i+1)]
            tmp_fun = fun1

        if tmp_fun < fun2:
            next_pairs = current_pairs[:ii] + current_pairs[ii+1:] + [(k, 2*i), (j, 2*i+1)]
            tmp_fun = fun2

    current_pairs = next_pairs
    current_fun = tmp_fun

print(current_pairs)
print(current_fun)
