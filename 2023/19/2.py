from os import stat
import re
import operator
from math import prod

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
                field, value = check.split("<")
                tests.append((field, "<", int(value), goto))
            else:
                field, value = check.split(">")
                tests.append((field, ">", int(value), goto))
        else:
            tests.append(("x", ">", 0, entry))
    workflows[name] = tests

def clamp(mod):
    if mod[0] > mod[1]:
        return [1, 0]  # empty interval lol
    return mod

def splitstate(part, test):
    INIT = prod(b-a+1 for (a, b) in part.values())
    part = dict(part)
    field, op, val, _ = test
    mod = part[field]
    mod1, mod0 = list(mod), list(mod)
    if op == ">":
        mod0[0] = max(mod0[0], val+1)
        mod1[1] = min(mod1[1], val)
    else:
        mod0[1] = min(mod0[1], val-1)
        mod1[0] = max(mod1[0], val)
    mod0 = clamp(mod0)
    mod1 = clamp(mod1)
    part0, part1 = dict(part), dict(part)
    part0[field] = mod0
    part1[field] = mod1
    E0 = prod(b-a+1 for (a, b) in part0.values())
    E1 = prod(b-a+1 for (a, b) in part1.values())
    assert E0 + E1 == INIT
    return part0, part1

def accepted(part, workflow):
    result = 0
    for test in workflow:
        taken, nottaken = splitstate(part, test)
        goto = test[3]
        if goto == "A":
            result += prod(b-a+1 for (a, b) in taken.values())
        elif goto == "R":
            result += 0
        else:
            result += accepted(taken, workflows[goto])
        part = nottaken
    return result


state = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
welp = accepted(state, workflows["in"])
print(welp)
