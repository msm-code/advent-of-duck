lines = open("input", "r").read().split("\n")
seeds = [int(x) for x in lines[0].split()[1:]]
new_seeds = list(seeds)
for l in lines[2:]:
    if 'map' in l:
        seeds, new_seeds = new_seeds, list(seeds)
        continue
    if l:
        dr, sr, ln = [int(x) for x in l.split()]
        for i, s in enumerate(seeds):
            if sr <= s < sr + ln:
                new_seeds[i] = s - sr + dr
print(min(new_seeds))
