data = open("input", "r").read().split("\n\n")
data = [[x for x in d.split("\n") if x] for d in data]

def ispalin(row, i):
    return row[:i][-min(i, len(row)-i):] == row[i:][:min(i, len(row)-i)][::-1]

def solve(x, ignore):
    for i in range(1, len(x[0])):
        if all(ispalin(row, i) for row in x) and i != ignore: return i
    for i in range(1, len(x)):
        if all(ispalin(row, i) for row in list(map(list, zip(*x)))) and i*100 != ignore: return i*100
    return 0

def solve2(w):
    s0 = solve(w, 0)
    for y in range(len(w)):
        for x in range(len(w[0])):
            w2 = [list(r) for r in w]
            w2[y][x] = {"#": ".", ".": "#"}[w2[y][x]]
            s1 = solve(w2, s0)
            if s1:
                return s1

print(sum(solve2(d) for d in data))
