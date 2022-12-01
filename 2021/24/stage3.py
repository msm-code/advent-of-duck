from functools import reduce

def prod(lst):
    return reduce(lambda a, b: a * b, lst)

STEPS = [
    (1, 14, 7),
    (1, 12, 4),
    (1, 11, 8),
    (26, -4, 1),
    (1, 10, 5),
    (1, 10, 14),
    (1, 15, 12),
    (26, -9, 10),
    (26, -9, 5),
    (1, 12, 7),
    (26, -15, 6),
    (26, -7, 8),
    (26, -10, 4),
    (26, 0, 6),
]

REDUCTIONS = [prod(d for (d, p0, p1) in STEPS[i:]) for i in range(len(STEPS))]

def dfs(v, step, out, digits):
    if step >= len(STEPS):
        if v == 0:
            print(out)
            exit()
        return
    if v > REDUCTIONS[step]:
        return
    (d, p0, p1) = STEPS[step]
    tmp = (v % 26) + p0
    v //= d
    for next in digits:
        if next != tmp:
            if d == 1:
                dfs((v * 26) + next + p1, step + 1, out * 10 + next, digits)
        else:
            dfs(v, step + 1, out * 10 + next, digits)
