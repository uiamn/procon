S = input()
res = ''

for c in S:
    res += chr(ord(c) - 32)

print(res)
