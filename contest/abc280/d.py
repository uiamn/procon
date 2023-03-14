K = int(input())
head = 1
tail = K

facttable = [1]
fact = 1

for i in range(1, 10**6+1):
    fact *= i
    fact %= K
    facttable.append(fact)

def factorial(n, mod):
    D = facttable
    N=n
    MOD=mod

    A=N//10 ** 6
    ans=D[A]
    B=N%10 ** 6
    for i in range(1,B+1):
        ans *= A*10 ** 6 + i
        ans %= MOD
    return ans

while tail - head > 1:
    pivot = (tail + head) // 2

    if factorial(pivot, K) == 0:
        tail = pivot
    else:
        head = pivot

print(tail)
