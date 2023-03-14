factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

result = 0
lefthand = lambda x: sum(map(lambda y: factorial[int(y)], str(x)))

for n in range(10, 10**7):
    if lefthand(n) == n:
        print(n)
        result += n

print(result)
