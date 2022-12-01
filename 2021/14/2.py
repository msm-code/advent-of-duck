import re
from collections import Counter, defaultdict

data = open('input').read()
polymer = data.split('\n')[0]
rules = re.findall("(.)(.) -> (.)", data)
rules = {(a, b): c for a, b, c in rules}

pairs = [x for x in zip(polymer, polymer[1:])]
pairs = {x: pairs.count(x) for x in pairs}

for i in range(40):
    newpairs = defaultdict(int)
    for (a, b), cnt in pairs.items():
        c = rules[(a, b)]
        newpairs[(a, c)] += cnt
        newpairs[(c, b)] += cnt
    pairs = newpairs

boys = defaultdict(int)
for (a, b), cnt in pairs.items():
    boys[a] += cnt
    boys[b] += cnt

cp = sorted(boys.items(), key=lambda x: x[1], reverse=True)
print((cp[0][1] - cp[-1][1] + 1) // 2)