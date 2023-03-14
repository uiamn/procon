N = int(input())
S = list(input())
T = list(input())

# S と T に含まれる 0 (1) の個数が異なると一致させられない
s_0 = 0
t_0 = 0
for i in range(N):
    s_0 += S[i] == '0'
    t_0 += T[i] == '0'

if s_0 != t_0:
    print(-1)
    exit(0)

ans = 0
for i in range(N):
    if S[i] == T[i]:
        continue
    elif T[i] == '1':  # つまり T[i] が 1 で S[i] が 0
        for j in range(i+1, N):
            if S[j] == '1':
                ans += j
                S[i] = '1'
                S[j] = '0'
                break
    else:  # T[i] が 0 で S[i] が 1
        for j in range(i+1, N):
            if S[j] == '0':
                ans += 1
                S[i] = '0'
                S[j] = '1'
                break

    print(''.join(S))

print(ans)


