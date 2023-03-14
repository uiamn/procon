facttable = []
po = 10 ** 6

def factorial(n, mod):
    D = facttable
    N=n
    MOD=mod

    ret = D[N//po]
    for i in range((N//po)*po+1, n+1):
        ret *= (ret*i) % MOD
        ret %= MOD

        if ret == 0:
            break

    return ret

def is_prime(q):
    if q % 2 == 0:
        return False

    i = 3
    while i**2 <= q:
        if q % i == 0:
            return False

        i += 2

    return True



def solve(k):
    K = k
    head = 1
    tail = K

    global facttable
    facttable = [1]
    fact = 1

    for i in range(1, po+1):
        fact *= i
        fact %= K
        facttable.append(fact)

    while tail - head > 1:
        pivot = (tail + head) // 2

        if factorial(pivot, K) == 0:
            tail = pivot
        else:
            head = pivot

    return tail


K = int(input())
ans = solve(K)
print(ans)
