def po(l):
    if len(l) == 2:
        return [[tuple(l)]]
    else:
        a = l[0]
        rest = l[1:]
        pa = []

        for i in range(len(rest)):
            for j in po(rest[:i] + rest[i+1:]):
                pa.append([(a, rest[i])] + j)

        return pa

print(po(list(range(8*2))))
