def hash(str):
    h = 0
    for c in str:
        h = ((h + ord(c)) * 17) % 256
    return h
data = open("input").read().strip().split(",")
boxes = [{} for x in range(256)]
for op in data:
    if '=' in op:
        label, val = op.split('=')
        boxes[hash(label)][label] = int(val)
    else:
        assert op.endswith('-')
        label = op[:-1]
        if label in boxes[hash(label)]:
            del boxes[hash(label)][label]
print(sum((i+1)*(1+p)*box[lens] for i, box in enumerate(boxes) for p, lens in enumerate(box)))
