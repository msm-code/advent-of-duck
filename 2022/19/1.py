import re
data = open("input").read()
blueprints = re.findall(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", data)

def solve_blueprint(blueprint_id, ore_for_orebot, ore_for_claybot, ore_for_obsibot, clay_for_obsibot, ore_for_geobot, obsi_for_geobot):
    def recur(time_left, ore_count, ore_bots, clay_count, clay_bots, obsi_count, obsi_bots, geo_count, geo_bots, best):
        if time_left <= 0:
            return geo_count

        simulated_geo_count = geo_count
        simulated_obsi_count = obsi_count
        simulated_geo_bots = geo_bots
        simulated_obsi_bots = obsi_bots
        for i in range(time_left):
            simulated_geo_count += simulated_geo_bots
            simulated_obsi_count += simulated_obsi_bots
            if simulated_obsi_count >= obsi_for_geobot:
                simulated_obsi_count -= obsi_for_geobot
                simulated_geo_bots += 1
            else:
                simulated_obsi_bots += 1
        if simulated_geo_count <= best:
            return 0

        new_ore_count = ore_count + ore_bots
        new_clay_count = clay_count + clay_bots
        new_obsi_count = obsi_count + obsi_bots
        new_geo_count = geo_count + geo_bots

        if ore_count >= ore_for_geobot and obsi_count >= obsi_for_geobot:
            best = max(best, recur(
                time_left - 1,
                new_ore_count - ore_for_geobot, ore_bots,
                new_clay_count, clay_bots,
                new_obsi_count - obsi_for_geobot, obsi_bots,
                new_geo_count, geo_bots + 1, best))
        if ore_count >= ore_for_obsibot and clay_count >= clay_for_obsibot:
            best = max(best, recur(
                time_left - 1,
                new_ore_count - ore_for_obsibot, ore_bots,
                new_clay_count - clay_for_obsibot, clay_bots,
                new_obsi_count, obsi_bots + 1,
                new_geo_count, geo_bots, best))
        if ore_count >= ore_for_claybot:
            best = max(best, recur(
                time_left - 1,
                new_ore_count - ore_for_claybot, ore_bots,
                new_clay_count, clay_bots + 1,
                new_obsi_count, obsi_bots,
                new_geo_count, geo_bots, best))
        if ore_count >= ore_for_orebot:
            best = max(best, recur(
                time_left - 1,
                new_ore_count - ore_for_orebot, ore_bots + 1,
                new_clay_count, clay_bots,
                new_obsi_count, obsi_bots,
                new_geo_count, geo_bots, best))
        best = max(best, recur(
            time_left - 1,
            new_ore_count, ore_bots,
            new_clay_count, clay_bots,
            new_obsi_count, obsi_bots,
            new_geo_count, geo_bots, best))

        return best

    return recur(24, 0, 1, 0, 0, 0, 0, 0, 0, 0)


total = 0

for bpdata in blueprints:
    bpdata = [int(i) for i in bpdata]
    total += bpdata[0] * solve_blueprint(*bpdata)

print(total)
