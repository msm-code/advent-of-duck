data = open("input", "r").read().split("\n\n")
data = [[x for x in d.split("\n") if x] for d in data]

def ispalin(row, i):
    return row[:i][-min(i, len(row)-i):] == row[i:][:min(i, len(row)-i)][::-1]

def solve(x):
    for i in range(1, len(x[0])):
        if all(ispalin(row, i) for row in x): return i
    for i in range(1, len(x)):
        if all(ispalin(row, i) for row in list(map(list, zip(*x)))): return i*100
    assert False

print(sum(solve(d) for d in data))
