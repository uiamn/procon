import itertools

def set_partitions(iterable, k=None):
    L = list(iterable)
    n = len(L)
    if k is not None:
        if k < 1:
            raise ValueError(
                "Can't partition in a negative or zero number of groups"
            )
        elif k > n:
            return

    def set_partitions_helper(L, k):
        n = len(L)
        if k == 1:
            yield [L]
        elif n == k:
            yield [[s] for s in L]
        else:
            e, *M = L
            for p in set_partitions_helper(M, k - 1):
                yield [[e], *p]
            for p in set_partitions_helper(M, k):
                for i in range(len(p)):
                    yield p[:i] + [[e] + p[i]] + p[i + 1 :]

    if k is None:
        for k in range(1, n + 1):
            yield from set_partitions_helper(L, k)
    else:
        yield from set_partitions_helper(L, k)

X = list(range(1, 10))
a = lambda x: int(''.join(map(str, x)))

result_set = set([])

for x in itertools.permutations(X):
    for p in set_partitions(x, 3):
        s, t, u = map(a, p)
        if s*t == u:
            result_set.add(u)

print(result_set)
print(sum(result_set))

