cache = {}

def f(n):
    if n == 0:
        return 1
    elif n in cache:
        return cache[n]
    else:
        val = f(n // 2) + f(n // 3)
        cache[n] = val
        return val

N = int(input())
print(f(N))
