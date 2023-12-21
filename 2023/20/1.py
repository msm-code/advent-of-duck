data = open("input", "r").read().strip().split("\n")

inputs = {}
states = {}
types = {}
machines = {}

for m in data:
    name, dest = m.split(" -> ")
    mtype, name = name[0], name[1:]
    types[name] = mtype
    machines[name] = []
    states[name] = 0
    for dst in dest.split(", "):
        if dst not in inputs:
            inputs[dst] = {}
        inputs[dst][name] = 0
        machines[name].append(dst)

def bcast(signals, machine, sig):
    for dst in machines[machine]:
        signals.append((machine, sig, dst))

SIGNALS = {0: 0, 1: 0}

def button():
    signals = [('button', 0, "roadcaster")]
    i = 0
    while i < len(signals):
        sigfrom, sig, machine = signals[i]
        SIGNALS[sig] += 1
        if machine not in types:
            pass
        elif types[machine] == 'b':
            bcast(signals, machine, sig)
        elif types[machine] == '%':
            if sig == 0:
                states[machine] = 1 - states[machine]
                bcast(signals, machine, states[machine])
        elif types[machine] == '&':
            inputs[machine][sigfrom] = sig
            bcast(signals, machine, 1 - all(inputs[machine].values()))
        else: assert False
        i += 1

for i in range(1000):
    button()
print(SIGNALS[0] * SIGNALS[1])
