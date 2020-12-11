import fileinput

# Part1

output = 0
adapter_ratings = sorted(int(n) for n in fileinput.input())
device_rating = adapter_ratings[-1] + 3
jolt_list = [output, *adapter_ratings, device_rating]

delta_list = [jolt_list[i+1] - jolt_list[i]
              for i in range(len(jolt_list)-1)]

p1 = delta_list.count(1) * delta_list.count(3)
print("Part 1:", p1)


# Part 2
# Using delta list from part1

table = {}


def n_combos(d_list):
    deltas = tuple(d_list)
    if len(deltas) <= 2:
        return 0
    elif deltas not in table:
        table[deltas] = n_combos(deltas[1:])
        if deltas[0] < 3 and deltas[1] == 1:
            table[deltas] += 1 + n_combos([deltas[0] + 1, *deltas[2:]])
    return table[deltas]


print("Part 2:", n_combos(delta_list) + 1)
