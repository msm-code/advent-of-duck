import yaml


class Monke:
    def __init__(self, name, elem):
        self.id = int(name.split()[1])
        if isinstance(elem["Starting items"], int):
            self.items = [elem["Starting items"]]
        else:
            self.items = [int(e) for e in elem["Starting items"].split(",")]
        self.test = int(elem["Test"].split()[2])
        self.iftrue = int(elem["If true"].split()[3])
        self.iffalse = int(elem["If false"].split()[3])
        self.optype = elem["Operation"].split()[3]
        self.opval = elem["Operation"].split()[4]
        self.inspections = 0
    
    def operation(self, item):
        old = item
        val = old if self.opval == "old" else int(self.opval)
        if self.optype == "*":
            return old * val
        else:
            return old + val


# if it's cursed but it works, it's the best kind of code
data = yaml.safe_load(open("input").read().replace("    ", "  "))
monkes = [Monke(k, v) for k, v in data.items()]

from math import prod
allmod = prod(m.test for m in monkes)
for _ in range(10000):
    for monke in monkes:
        for item in monke.items:
            monke.inspections += 1
            item = monke.operation(item)
            item %= allmod
            test = item % monke.test
            if test == 0:
                monkes[monke.iftrue].items.append(item)
            else:
                monkes[monke.iffalse].items.append(item)
        monke.items = []

inspections = sorted(m.inspections for m in monkes)[-2:]
print(inspections[0] * inspections[1])
