x = open("input", "r").read().split("\n")
x = [(l.split(" ")[0], [int(c) for c in l.split(" ")[1].split(",")]) for l in x if l]

def solve(pat, lens):
    if not lens:
        if "#" in pat: return 0
        return 1
    if not pat or len(pat) < lens[0]:
        return 0
    l0 = lens[0]
    can = all(c in "?#" for c in pat[:l0]) and (len(pat) == l0 or pat[l0] in '?.')
    opts = 0
    if can:
        opts += solve(pat[l0+1:], lens[1:])
    if pat[0] != "#":
        opts += solve(pat[1:], lens)
    return opts

print(sum(solve(*e) for e in x))

