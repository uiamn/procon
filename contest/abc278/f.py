def mex(l):
    for i in range(51*51):
        if i not in l:
            return i

def hash(l):
    return ''.join(map(str, l))

cache = {}
def grundy(s, rest_indexes, Ss):
    a = cache.get(hash(rest_indexes))

    if a is not None:
        return a
    else:
        candidate = set([])
        for i in rest_indexes:
            if s is None or s[-1] == Ss[i][0]:
                next_rest_indexes = [j for j in rest_indexes if i != j]
                candidate.add(grundy(Ss[i], next_rest_indexes, Ss))

        g = mex(candidate)
        cache[hash(rest_indexes)] = g
        return g

N = int(input())
Ss = []
rest_index = [i for i in range(N)]

for _ in range(N):
    Ss.append(input())

g = grundy(None, rest_index, Ss)
if g == 0:
    print('Second')
else:
    print('First')

