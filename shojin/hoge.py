cache = {}
def f(n, popcount_in=None):
    if n in cache:
        return cache[n]

    if popcount_in is None:
        popcount = calc_popcount(n)
    else:
        popcount = popcount_in

    if n % popcount == 0:
        cache[n] = 1
        return 1
    else:
        result = 1 + f(n % popcount)
        cache[n] = result
        return result


def calc_popcount(n):
    popcount = 0
    while n:
        popcount += n & 1
        n >>= 1

    return popcount

N = int(input())
X = int(input(), 2)
Xpopcount = calc_popcount(X)

for i in range(N):
    if (X >> (N-i-1) & 1):
        pop = Xpopcount - 1
    else:
        pop = Xpopcount + 1
    print(f(X ^ (1 << (N-i-1)), pop))

