import sys
sys.setrecursionlimit(100000)

def solve(s: str) -> bool:
    if len(s) <= 1:
        return True
    elif len(s) == 2:
        return s[0] == s[1]
    elif len(s) == 3:
        if s == 'AAB' or s == 'ABB':
            return False
        else:
            return True
    elif s[0] == 'A' and s[-1] == 'B':
        return False
    elif s[0] == 'B' and s[-1] == 'A':
        next_s = s[1:-2] + 'A'
        return solve(next_s)
    elif s[0] == 'A' and s[-1] == 'A':
        if s[1] == 'A':
            next_s = 'B' + s[2:-1]
            return solve(s[1:-1]) or solve(next_s)
        else:
            return solve(s[1:-1])
    else:
        if s[-2] == 'B':
            next_s = s[1:-2] + 'A'
            return solve(s[1:-1]) or solve(next_s)
        else:
            return solve(s[1:-1])


N = int(input())
S = input()

print('Yes' if solve(S) else 'No')
