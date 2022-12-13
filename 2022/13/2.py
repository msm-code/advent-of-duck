import ast
from functools import cmp_to_key

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

pairdata = open("input").read().strip().split()
pairs = [ast.literal_eval(pair) for pair in pairdata]
pairs += [[[2]]] + [[[6]]]
pairs.sort(key=cmp_to_key(compare), reverse=True)
print((1+pairs.index([[2]]))*(1+pairs.index([[6]])))
