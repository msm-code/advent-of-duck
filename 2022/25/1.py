def snafu_to_int(s):
    total = 0
    for c in s:
        val = {
            "2": 2,
            "1": 1,
            "0": 0,
            "-": -1,
            "=": -2,
        }
        total = total * 5 + val[c]
    return total

def int_to_snafu(num):
    result = ""
    carry = 0
    while num != 0 or carry != 0:
        rem = (num % 5) + carry
        if rem == 3:
            carry = 1
            result = "=" + result
        elif rem == 4:
            carry = 1
            result = "-" + result
        elif rem == 5:
            carry = 1
            result = "0" + result
        else:
            carry = 0
            result = str(rem) + result
        num //= 5
    return result

data = open("input").read().split()
total = sum(snafu_to_int(n) for n in data)
print(int_to_snafu(total))
