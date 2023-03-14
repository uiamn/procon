S = input()
T = input()

for i in range(len(S) - len(T) + 1):
    if T == S[i:i+len(T)]:
        print('Yes')
        exit(0)

print('No')
