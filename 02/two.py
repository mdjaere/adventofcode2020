with open("input.txt") as file:
    lines = file.read().split("\n")

data_list = [line.split(": ") for line in lines]

valid_count = 0
for data in data_list:
    [rule_raw, password] = data
    [range_raw, letter] = rule_raw.split(" ")
    [first_loc, second_loc] = [int(loc) - 1 for loc in range_raw.split("-")]
    if password[first_loc] == password[second_loc]:
        continue
    elif password[first_loc] == letter:
        valid_count += 1
    elif password[second_loc] == letter:
        valid_count += 1
print(f"There are {valid_count} valid passwords")
