N = int(input())
A = {}
tmpA = map(int, input().split())
for i, a in enumerate(tmpA):
    A[i+1] = a

Q = int(input())
last_1_query_val = 0

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        last_1_query_val = q[1]
        A = {}
    elif q[0] == 2:
        i = q[1]
        x = q[2]
        if i in A:
            A[i] += x
        else:
            A[i] = x
    else:
        i = q[1]
        if i in A:
            print(last_1_query_val + A[i])
        else:
            print(last_1_query_val)

