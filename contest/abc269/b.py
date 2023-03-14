A = None
B = None
C = None
D = None

for i in range(1, 11):
    s = input()
    if s == '..........':
        pass
    else:
        if A is None:
            A = i
            for j, c in enumerate(s + '.'):
                if c == '#' and C is None:
                    C = j+1
                elif C is not None and D is None and c == '.':
                    D = j
        else:
            B = i

print(f'{A} {B if B is not None else A}\n{C} {D}')
