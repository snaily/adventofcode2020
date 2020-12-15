import sys
import re

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

fourdigits_pattern = re.compile(r'^(\d{4})$')
def byr(value):
    if not fourdigits_pattern.match(value):
        return False
    return 1920 <= int(value) <= 2002
def iyr(value):
    if not fourdigits_pattern.match(value):
        return False
    return 2010 <= int(value) <= 2020
def eyr(value):
    if not fourdigits_pattern.match(value):
        return False
    return 2020 <= int(value) <= 2030
hgt_pattern = re.compile(r'^(\d+)(in|cm)$')
def hgt(value):
    match = hgt_pattern.match(value)
    if not match:
        return False
    quantity, unit = match.groups()
    if unit == 'cm':
        return 150 <= int(quantity) <= 193
    else:
        return 59 <= int(quantity) <= 76
hcl_pattern = re.compile(r'^#[0-9a-f]{6}$')
def hcl(value):
    return bool(hcl_pattern.match(value))
ecl_valid = set(('amb','blu','brn','gry','grn','hzl','oth'))
def ecl(value):
    return value in ecl_valid
pid_pattern = re.compile(r'^[0-9]{9}$')
def pid(value):
    return bool(pid_pattern.match(value))
def cid(value):
    return True

VALIDATORS = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
    'cid': cid,
}

valid = 0
fields_seen = set()
field_error = False
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        if line == '':
            if (len(fields_seen) == 8 or (len(fields_seen) == 7 and not 'cid' in fields_seen)) and not field_error:
                valid += 1
            field_error = False
            fields_seen.clear()
            continue
        pairs = line.split(' ')
        for pair in pairs:
            field, value = pair.split(':')
            fields_seen.add(field)
            if not VALIDATORS[field](value):
                print('invalid',field, value)
                field_error = True

print(valid)