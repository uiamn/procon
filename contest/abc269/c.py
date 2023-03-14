import itertools


X = int(input())

binX = bin(X)[2:]
binX = ''.join(['0' for _ in range(60-len(binX))]) + binX

one_digit = []

for i in range(60):
    if binX[-(i+1)] == '1':
        one_digit.append(i)

for b in range(2**len(one_digit)):
    x = 0
    for i in range(len(one_digit)):
        if (b >> i) & 1:
            x += (2**one_digit[i])

    print(x)
