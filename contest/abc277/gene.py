from random import randint

N = 20
M = 10
a = randint(0, M)
A = []
for i in range(N):
    A.append(str((a+2*i) % M))

print(f'{N} {M}\n{" ".join(A)}')
