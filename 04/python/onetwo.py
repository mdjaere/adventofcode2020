
with open("input.txt") as file:
    raw = file.read()

passports = [passport.strip().replace("\n", " ") for passport in raw.split("\n\n")]

req_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid") # leaving out cid

def check_passport_fields(p, req_fields):
    fields = p.split()
    keys = map( lambda x: x.split(":")[0] , fields)
    valid = list(filter( lambda x: x in req_fields, keys ))
    return len(valid) >= len(req_fields)

def is_valid(k, v):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    if k == "byr":
        return 1920 <= int(v) <= 2002
    elif k == "iyr":
        return 2010 <= int(v) <= 2020
    elif k == "eyr":
        return 2020 <= int(v) <= 2030
    elif k == "hgt":
        if v.endswith("cm"):
            return 150 <= int(v[0:-2]) <= 193
        elif v.endswith("in"):
            return 59 <= int(v[0:-2]) <= 76
        else:
            return False
    elif k == "hcl":
        return v.startswith("#") and all([c in "0123456789abcdef" for c in v[1:]])
    elif k == "ecl":
        return v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif k == "pid":
        return len(v)==9 and all([c in "0123456789" for c in v])
    else:
        return True

def check_field_values(p):
    fields = p.split()
    for field in fields:
        if not is_valid(*field.split(":")):
            return False
    return True
 
valid_one = sum([check_passport_fields(p, req_fields) for p in passports])
valid_two = sum([check_passport_fields(p, req_fields) and check_field_values(p) for p in passports])

print( f"Task one: {valid_one}")
print( f"Task two: {valid_two}")