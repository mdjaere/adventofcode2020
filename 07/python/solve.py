import itertools

bag_rules = [[item.replace(" bags", "").replace(" bag", "").strip() for item in line.strip(".\n").split(
    " contain ")] for line in open("input.txt")]

# Part 1


def find_parents(bags, bag_type):
    bags = []
    for line in bag_rules:
        if bag_type in line[1]:
            bags.append(line)
    return bags


def find_all(bag_rules, bag_type):
    filtered_rules = find_parents(bag_rules, bag_type)
    if not filtered_rules:
        return []
    else:
        new_bag_types = [rule[0] for rule in filtered_rules]
        new_p = [find_all(bag_rules, new) for new in new_bag_types]
        return filtered_rules + list(itertools.chain.from_iterable(new_p))


sol = find_all(bag_rules, "shiny gold")
p1 = set([b[0] for b in sol])
print("Part 1:", len(p1))

# Part 2


def find_count_and_children(bag_rules, bag_type):
    count = []
    child_types = []
    for bag_rule in filter(lambda rule: bag_type in rule[0], bag_rules):
        for child in bag_rule[1].split(", "):
            if child[0].isdigit():
                count.append(int(child[0]))
                child_types.append(child[2:])
    return count, child_types


def count_all(bag_rules, bag_type, multiplier=1):
    count, child_types = find_count_and_children(bag_rules, bag_type)
    if sum(count) == 0:
        return [0]
    else:
        child_count = [count_all(bag_rules, b_type, multiplier * b_count)
                       for b_count, b_type in zip(count, child_types)]
        return [sum(count) * multiplier] + list(itertools.chain.from_iterable(child_count))


p2 = sum(count_all(bag_rules, "shiny gold"))
print("Part 2:", p2)
