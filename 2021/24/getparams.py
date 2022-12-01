import re

data = [l.split() for l in open("input").read().split("\n") if l]

for opcode, *params in data:
    if opcode == "div":
        print("d  =", params[1])
    elif opcode == "add" and params[0] == "x" and re.match("-?[0-9]+", params[1]):
        print("p0 =", params[1])
    elif opcode == "add" and params[0] == "y" and re.match("-?[0-9]+", params[1]) and params[1] not in ["25", "1"]:
        print("p1 =", params[1])