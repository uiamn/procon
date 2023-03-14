result = 0
for i in range(1, 7):
    for j in range(10**(i-1), min((9**5)*i+1, 10**i)):
        s = 0
        for x in map(int, str(j)):
            s += x**5

        if s == j:
            result += j

print(result-1)
