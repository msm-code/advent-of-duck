data = [x.split(": ") for x in open("input", "r").read().split("\n") if x]
monkes = {}
while "root" not in monkes:
    for name, command in data:
        if command.isdigit():
            monkes[name] = int(command)
        else:
            try:
                monkes[name] = eval(command, monkes)
            except:
                pass
print(int(monkes["root"]))
