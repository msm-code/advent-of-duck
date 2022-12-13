import ast

def compare(i, j):
    if isinstance(i, int) and isinstance(j, int):
        return j - i  # positive = ok order, negative = bad order
    if isinstance(i, list) and isinstance(j, int):
        j = [j]
    if isinstance(i, int) and isinstance(j, list):
        i = [i]
    for it in range(len(i)):
        if it >= len(j):
            return -1  # wrong order
        cmp = compare(i[it], j[it])
        if cmp != 0:
            return cmp
    if len(i) < len(j):
        return 1
    return 0

pairdata = open("input").read().strip().split("\n\n")
pairs = [[ast.literal_eval(l) for l in pair.split("\n")] for pair in pairdata]
ok = 0
for i, (l, r) in enumerate(pairs):
    ok += i+1 if compare(l, r) > 0 else 0
print(ok)
