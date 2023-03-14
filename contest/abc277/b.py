N = int(input())
Ss = set([])

for _ in range(N):
    S = input()

    if not S[0] in 'HDCS':
        print('No')
        exit(0)

    if not S[1] in 'A23456789TJQK':
        print('No')
        exit(0)

    if S in Ss:
        print('No')
        exit(0)

    Ss.add(S)

print('Yes')
