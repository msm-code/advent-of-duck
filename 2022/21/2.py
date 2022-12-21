data = dict(x.split(": ") for x in open("input", "r").read().split("\n") if x)
del data["humn"]
monkes = {}

def follow(root, value):
    while root != "humn":
        lhs, op, rhs = data[root].split()
        if lhs in monkes:
            root, val, flip = rhs, int(monkes[lhs]), False
        else:
            root, val, flip = lhs, int(monkes[rhs]), True
        if op == '+':
            value = value - val
        elif op == '-':
            value = value + val if flip else val - value
        elif op == '*':
            value = value / val
        elif op == '/':
            value = value * val if flip else val / value
    return int(value)

for i in range(30):  # technically, loop until no new monkes
    for name, command in data.items():
        if command.isdigit():
            monkes[name] = int(command)
        else:
            try:
                monkes[name] = eval(command, monkes)
            except:
                pass

nameA, _, nameB = data["root"].split(" ")
result = follow(nameB, monkes[nameA]) if nameA in monkes else follow(nameA, monkes[nameB])
print(result)    
