def solve(N, A, B):
    if N < A:
        print(0)
        return

    if A <= B:
        print(N-A+1)
        return


    if N % A == 0:
        ans = (N // A - 1) * B + 1
    elif N % A >= B:
        ans = (N // A) * B
    else:
        ans = (N // A - 1) * B + N - (N // A) * A + 1

    print(ans)

N, A, B = map(int, input().split())
solve(N, A, B)
