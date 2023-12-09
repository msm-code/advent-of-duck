data = [[int(c) for c in l.split()] for l in open("input", "r").read().split("\n") if l]

def extrapolate(row):
    if not any(row): return 0
    return row[0] - extrapolate([b - a for a, b in zip(row, row[1:])])

print(sum(extrapolate(row) for row in data))
