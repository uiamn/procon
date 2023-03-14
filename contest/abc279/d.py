from math import sqrt

A, B = map(int, input().split())
asq = A ** 2
bsq = B ** 2

f = lambda t: t*B + (A / sqrt(1+t))

head = 0
tail = 10 ** 18

while tail - head > 1:
    n = (head + tail) // 2
    if (A / sqrt(n+2) - A / sqrt(n+1) + B) < 0:
        head = n
    else:
        tail = n

print(min(f(head), f(tail)))
