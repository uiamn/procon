import re
ptn = re.compile(r'[a-z]*okyo[a-z]*ech[a-z]*')

N = int(input())

for _ in range(N):
    S = input()

    if re.match(ptn, S):
        print('Yes')
    else:
        print('No')
