MOD = 10 ** 9 + 7
S = input()
acounts = []  # acounts[i] = S の 1 文字目から i 文字目までに含まれる a と ? の数
ccounts = []  # ccounts[i] = S の 1 文字目から i 文字目までに含まれる c と ? の数

acount = 0
ccount = 0

for c in S:
    if c == 'A':
        acount += 1
    elif c == 'C':
        ccount += 1
    elif c == '?':
        acount += 1
        ccount += 1

    acounts.append(acount)
    ccounts.append(ccount)

print(acounts)
print(ccounts)

ans = 0
for i in range(1, len(S)):
    c = S[i]
    if c == 'B' or c == '?':
        ans += (acounts[i-1]) * (ccounts[-1] - ccounts[i])

        ans %= MOD

print(ans)
