from os import stat
import re
import operator

data = open("input").read()
code, parts = data.split("\n\n")
code, parts = code.strip().split("\n"), parts.strip().split("\n")

workflows = {}
for l in code:
    name, body = re.match("([a-z]+){(.*)}", l).groups()
    tests = []
    for entry in body.split(","):
        if ":" in entry:
            check, goto = entry.split(":")
            if "<" in check:
                (field, value), op = check.split("<"), operator.lt
            else:
                (field, value), op = check.split(">"), operator.gt
            def ehh(op, field, value): return lambda g: op(g[field], int(value))
            tests.append((ehh(op, field, value), goto))
        else:
            tests.append(((lambda g: True), entry))
    workflows[name] = tests

def check(part, state):
    if state == "A": return True
    if state == "R": return False
    for (test, next) in workflows[state]:
        if test(part):
            return check(part, next)

parts = [dict(zip("xmas", [int(i) for i in re.match("{x=(\\d+),m=(\\d+),a=(\\d+),s=(\\d+)}", l).groups()])) for l in parts]
total = 0
for part in parts:
    if check(part, "in"):
        total += sum(part.values())

print(total)
    



# print(code, parts)
