N = int(input())
_ = input()
A = list(map(int, input().split()))

head = 1
tail = 10**4+1

while tail - head > 1:
    k = (head + tail) // 2

    for i in range(N):
        if abs(A[i] - A[i+1]) >= k or (A[i] % k) == (A[i+1] % k):
            continue
        else:
            break
    else:
        head = k
        continue

    tail = k

f = lambda k: lambda x: [x//k +1 for _ in range(x % k)] + [x//k for _ in range(k - (x%k))]

anstmp = list(map(f(head), A))
answer = []

for i in range(head):
    tmp = []
    for a in anstmp:
        tmp.append(str(a[i]))

    answer.append(' '.join(tmp))

print(head)
for ans in answer:
    print(ans)
