import re
from collections import Counter

data = open('input').read()
polymer = data.split('\n')[0]
rules = re.findall("(.)(.) -> (.)", data)
rules = {(a, b): c for a, b, c in rules}

for i in range(10):
    polymer = polymer[0] + "".join(rules[(a, b)] + b for (a, b) in zip(polymer, polymer[1:]))

cp = Counter(polymer).most_common()
print(cp[0][1] - cp[-1][1])