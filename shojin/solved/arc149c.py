N = int(input())

if N >= 6:
    odd = []
    even = []
    special_odd = []
    special_even = []

    for i in range(1, N**2 + 1):
        if i % 2 == 0:
            if i % 3 == 0 and len(special_even) < N:
                special_even.append(i)
            else:
                even.append(i)
        else:
            if i % 3 == 0 and len(special_odd) < N:
                special_odd.append(i)
            else:
                odd.append(i)

    if N % 2 == 0:
        for i in range(N):
            for j in range(N):
                if i <= N // 2 - 2:
                    print(even.pop(), end='')
                elif i == N // 2 - 1:
                    print(special_even.pop(), end='')
                elif i == N // 2:
                    print(special_odd.pop(), end='')
                else:
                    print(odd.pop(), end='')

                if j == N-1:
                    print()
                else:
                    print(' ', end='')
    else:
        for i in range(N):
            for j in range(N):
                if i <= N // 2 - 2:
                    print(even.pop(), end='')
                elif i == N // 2 - 1:
                    if j <= N // 2 - 1:
                        print(even.pop(), end='')
                    else:
                        print(special_even.pop(), end='')
                elif i == N // 2:
                    if j <= N // 2 - 1:
                        print(special_even.pop(), end='')
                    else:
                        print(special_odd.pop(), end='')
                elif i == N // 2 + 1:
                    if j <= N // 2 - 1:
                        print(special_odd.pop(), end='')
                    else:
                        print(odd.pop(), end='')
                else:
                    print(odd.pop(), end='')

                if j == N-1:
                    print()
                else:
                    print(' ', end='')
elif N == 3:
    print('4 2 6')
    print('8 7 3')
    print('1 5 9')
elif N == 4:
    print('10 12 14 16')
    print('2 4 6 8')
    print('7 5 3 1')
    print('9 11 13 15')
elif N == 5:
    print('16 18 20 22 24')
    print('14 12 10 8 6')
    print('2 4 5 7 9')
    print('13 11 1 3 15')
    print('17 19 21 23 25')
