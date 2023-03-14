from typing import List
from itertools import permutations

def smallest_prime_factors(N: int) -> List[int]:
    spf = [i for i in range(N+1)]

    i = 2
    while i*i <= N:
        if spf[i] == i:  # spf[i] == i <-> i は素数
            for j in range(i*i, N+1, i):
                if spf[j] == j:
                    spf[j] = i

        i += 1

    return spf

def factolization(n: int) -> List[int]:
    factors = []
    m = n

    while spf[m] != m:
        factors.append(spf[m])
        m //= spf[m]
    else:
        factors.append(m)

    return factors


N = int(input())

if N == 1:
    print(0)
    exit(0)

spf = smallest_prime_factors(N)

exponents = {}

for n in range(2, N+1):
    pfs = factolization(n)
    po = {}
    for p in pfs:
        if p in exponents:
            exponents[p] += 1
        else:
            exponents[p] = 1

exps = list(exponents.values())
answer = 0

for q in exps:
    if q >= 74:
        answer += 1

for i, j in permutations(range(len(exps)), 2):
    p = exps[i]
    q = exps[j]

    if p >= 24 and q >= 2:
        answer += 1

    if p >= 14 and q >= 4:
        answer += 1

    if p >= 4 and q >= 4 and i < j:
        for k in range(len(exps)):
            if k != i and k != j and exps[k] >= 2:
                answer += 1

print(answer)
