import random
from typing import List

N = 8


def is_valid(seq: List[int]) -> bool:
    is_asc = True
    for i in range(len(seq)-1):
        if (is_asc and seq[i] < seq[i+1]) or (not is_asc and seq[i] > seq[i+1]):
            continue
        elif is_asc:
            is_asc = False
        else:
            return False

    return True


def search(seq: List[int]) -> List[bool]:
    maxlen = 0
    max_subseq_index = None

    for b in range(1, 2**N):
        cand_subseq = []
        for i in range(N):
            if (b >> i) & 1 == 1:
                cand_subseq.append(seq[N-i-1])

        if len(cand_subseq) <= maxlen:
            continue

        if is_valid(cand_subseq):
            maxlen = len(cand_subseq)
            max_subseq_index = b

    res = []
    for i in range(N):
        if (max_subseq_index >> i) & 1 == 1:
            res.append(N-i-1)

    return res

instance = list(range(1, N+1))
for _ in range(16):
    random.shuffle(instance)
    result = search(instance)

    print(' '.join(map(str, instance)), " => ", end='')

    for i, p in enumerate(instance):
        if i in result:
            print(f'\033[31m{p}\033[0m', end=' ')
        else:
            print(p, end=' ')

    print()
