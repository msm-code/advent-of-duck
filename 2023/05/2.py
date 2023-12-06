lines = open("input", "r").read().split("\n")
seeds_raw = [int(x) for x in lines[0].split()[1:]]
untransformed = [(seeds_raw[i*2], seeds_raw[i*2]+seeds_raw[i*2+1]-1) for i in range(len(seeds_raw)//2)]
transformed = []

def intersect(a, b):
    """Returns a tuple (list_of_intersecting_ranges, list_of_nonintersecting_ranges)"""
    a0, a1 = a
    b0, b1 = b
    if a1 < b0 or a0 > b1:
        return ([], [(a0, a1)])
    if b0 <= a0 and b1 >= a1:
        return ([(a0, a1)], [])
    if b0 <= a0 and b1 < a1:
        return ([(a0, b1)], [(b1+1, a1)])
    if b0 > a0 and b1 >= a1:
        return ([(b0, a1)], [(a0, b0-1)])
    if b0 > a0 and b1 < a1:
        return ([(b0, b1)], [(a0, b0-1), (b1+1, a1)])
    assert False

assert intersect((1, 4), (100, 101)) == ([], [(1, 4)])  # case 0: nontouching
assert intersect((1, 4), (0, 5)) == ([(1, 4)], []) # case 1: a in b
assert intersect((1, 4), (0, 2)) == ([(1, 2)], [(3, 4)]) # case 2: left intersect
assert intersect((1, 4), (3, 5)) == ([(3, 4)], [(1, 2)]) # case 3: right intersect
assert intersect((1, 4), (2, 3)) == ([(2, 3)], [(1, 1), (4, 4)]) # case 4: b in a

for l in lines[2:]:
    if 'map' in l:
        untransformed += transformed
        transformed = []
        continue
    if not l:
        continue
    dr, sr, ln = [int(x) for x in l.split()]
    new_untransformed = []
    for s in list(untransformed):
        new_t, new_u = intersect(s, (sr, sr+ln))
        new_untransformed += new_u
        transformed += [[t-sr+dr for t in tset] for tset in new_t]
    untransformed = new_untransformed

untransformed += transformed
print(min(u[0] for u in untransformed))
