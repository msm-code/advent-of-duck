import operator
data = bytes.fromhex(open('input').read())


# Discriminated unions, where are you when i need you
class Packet:
    def __init__(self, version, tid, body, op):
        self.version = version
        self.tid = tid
        self.body = body  # body is either integer or a list of packets
        self.op = op

    def fold(self):
        if self.op is None:
            return self.body
        else:
            acc = self.body[0].fold()
            for node in self.body[1:]:
                acc = self.op(acc, node.fold())
        return acc


def bits(data):
    for c in data:
        for b in f"{c:08b}":
            yield int(b)


class BitStream:
    def __init__(self, data):
        self.bits = bits(data)
        self.pos = 0

    def get(self, n):
        """ read bits in big endian """
        self.pos += n
        return int("".join(str(next(self.bits)) for _ in range(n)), 2)


def parse_literal(it):
    out = 0
    while True:
        chunk = it.get(5)
        out = (out << 4) + (chunk & 0xF)
        if chunk <= 0xF:
            return out


def parse_operation(it):
    ltid = it.get(1)
    children = []
    if ltid == 0:
        length = it.get(15)
        end_pos = it.pos + length
        while it.pos < end_pos:
            children.append(parse(it))
        assert it.pos == end_pos
    else:
        chunks = it.get(11)
        for i in range(chunks):
            children.append(parse(it))
    return children


def parse(it):
    version = it.get(3)
    tid = it.get(3)
    operators = {
        0: lambda a, b: a + b,
        1: lambda a, b: a * b,
        2: lambda a, b: min(a, b),
        3: lambda a, b: max(a, b),
        4: None,
        5: lambda a, b: a > b,
        6: lambda a, b: a < b,
        7: lambda a, b: a == b,
    }
    if tid == 4:
        body = parse_literal(it)
    else:
        body = parse_operation(it)
    return Packet(version, tid, body, operators[tid])


tree = parse(BitStream(data))
print(tree.fold())