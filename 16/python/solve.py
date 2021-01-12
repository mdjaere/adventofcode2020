import fileinput
from collections import Counter
from functools import reduce

lines = [line.strip("\n ") for line in fileinput.input()]

rules = {}
my_ticket = []
other_tickets = []


# PARSING

section = 0
for line in lines:
    if line == "":
        section += 1
        continue
    if section == 0:
        # RULES
        category, ranges_raw = line.split(": ")
        ranges = [tuple([int(v) for v in rule_raw.split("-")])
                  for rule_raw in ranges_raw.split(" or ")]
        rules[category] = ranges
    elif section == 1:
        # MY TICKET
        if not "your ticket" in line:
            my_ticket = tuple(int(v) for v in line.split(","))
    elif section == 2:
        # OTHER TICKETS
        if not "nearby tickets" in line:
            other_tickets.append(tuple(int(v) for v in line.split(",")))

# PART 1


def get_category(value):
    found = []
    for category in rules.keys():
        ranges = rules[category]
        for r in ranges:
            if r[0] <= value <= r[1]:
                found.append(category)
    return found


invalid_numbers = []
valid_tickets = []

for ticket in other_tickets:
    invalid_ticket = False
    for number in ticket:
        categories = get_category(number)
        if not categories:
            invalid_ticket = True
            invalid_numbers.append(number)
    if not invalid_ticket:
        valid_tickets.append(ticket)

print("Part1:", sum(invalid_numbers))

# Part 2

category_map = {cat: [] for cat in rules.keys()}
category_found = [None] * len(category_map)

# mapping possible category indexes

for ticket in valid_tickets:
    for i, number in enumerate(ticket):
        categories = get_category(number)
        for cat in categories:
            category_map[cat].append(i)

# Solving Sudoku

cats = dict(category_map)

while cats:
    found = False
    for category, values in cats.items():
        all_counts = Counter(values)
        vals = list(all_counts.values())
        for ticket_index, n in all_counts.items():
            if n == max(vals) and vals.count(n) == 1:
                category_found[ticket_index] = category
                found = True
                break
        if found:
            break
    cats = {cat: [val for val in values if val != ticket_index]
            for cat, values in cats.items() if cat != category}

departure_results = [my_ticket[i]
                     for i, cat in enumerate(category_found) if "departure" in cat]

print("Part2:", reduce(lambda a, b: a*b, departure_results))
