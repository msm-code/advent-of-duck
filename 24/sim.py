import re
import sys
vars = {v: 0 for v in "xyzw"}

data = [l.split() for l in open("input").read().split("\n") if l]
INPUT = [int(i) for i in sys.argv[1]]

for i, (opcode, *params) in enumerate(data):
    var = f"v{i}"
    if opcode == "inp":
        vars[params[0]] = INPUT[0]
        INPUT = INPUT[1:]
        continue
    lvalue = vars[params[0]]
    if re.match("-?[0-9]+", params[1]):
        rvalue = int(params[1])
    else:
        rvalue = vars[params[1]]

    if opcode == "mul":
        out = lvalue * rvalue
    elif opcode == "add":
        out = lvalue + rvalue
    elif opcode == "mod":
        out = lvalue % rvalue
    elif opcode == "div":
        out = lvalue // rvalue
    elif opcode == "eql":
        out = int(lvalue == rvalue)
    vars[params[0]] = out

for reg, val in vars.items():
    print(f"{reg} = {val}")