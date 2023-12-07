from collections import Counter

def card_type(card):
    trace = sorted(Counter(card).values())
    return {
        (5,): 1,
        (1, 4): 2,
        (2, 3): 3,
        (1, 1, 3): 4,
        (1, 2, 2): 5,
        (1, 1, 1, 2): 6,
        (1, 1, 1, 1, 1): 7,
    }[tuple(trace)]

def card_to_value(card):
    t = ["AKQJT98765432".index(c) for c in card]
    return [card_type(card)] + t

cards = [(l.split()[0], int(l.split()[1])) for l in open("input", "r").read().split("\n") if l]
print(sum((i+1)*v for i, (k, v) in enumerate(sorted(cards, reverse=True, key=lambda k: card_to_value(k[0])))))
