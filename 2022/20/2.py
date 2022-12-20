data0 = [int(x) for x in open("input").read().split()]
data = list(enumerate(data0))

DECRYPTION_KEY = 811589153
for j in range(10):
    for i in range(len(data)):
        tuple_index = -1
        for tuple_index in range(len(data)):
            if data[tuple_index][0] == i:
                break
        tuple_value = data[tuple_index][1]

        if tuple_value > 0:
            tuple_value = (tuple_value * DECRYPTION_KEY) % (len(data) - 1)
            for _ in range(tuple_value):
                if tuple_index == len(data) - 1:
                    data = [data[-1]] + data[:-1]
                    tuple_index = 1
                else:
                    tuple_index += 1
                data = data[:tuple_index-1] + [data[tuple_index], data[tuple_index-1]] + data[tuple_index+1:]
        if tuple_value < 0:
            tuple_value = -(-(tuple_value * DECRYPTION_KEY) % (len(data) - 1))
            for _ in range(-tuple_value):
                if tuple_index == 0:
                    data = data[1:] + [data[0]]
                    tuple_index = len(data) - 2
                else:
                    tuple_index -= 1
                data = data[:tuple_index] + [data[tuple_index+1], data[tuple_index]] + data[tuple_index+2:]

zerondx = next(i for (i, (oi, v)) in enumerate(data) if v == 0)
sums = 0
for i in [1000, 2000, 3000]:
    sums += data[(zerondx + i) % len(data)][1]
print(sums * DECRYPTION_KEY)
