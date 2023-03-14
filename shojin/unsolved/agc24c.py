N = int(input())
A = []

for _ in range(N):
    A.append(int(input()))

if A[0] != 0:
    print(-1)
    exit(0)

seqs = []

i = 0
while i < N-1:
    seq = [A[i]]
    j = 1

    while i+j < N:
        if seq[-1] + 1 == A[i+j]:
            seq.append(A[i+j])
            j += 1
        else:
            break

    seqs.append(seq)
    i += j

lasttail = 0
ans = 0
for seq in seqs:
    if lasttail < seq[0]:
        print(-1)
        exit(0)

    ans += seq[0] + len(seq) - 1
    lasttail = seq[-1]

print(ans)
