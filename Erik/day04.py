import re
password_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
check_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("Advent-of-Code-2020/Erik/inputs/day04.txt", "r") as f:
#with open("Advent-of-Code-2020/Erik/inputs/day04-t1.txt", "r") as f:
    raw_data2 = f.read().split("\n\n")

def make_dict(raw):
    dict_list = []
    listed_data = [x.split() for x in raw]
    for passport in listed_data:
        temp_dict = dict()
        for line in passport:
            key, val = line.split(":", 1)
            temp_dict.update({key:val})
        dict_list.append(temp_dict)
    return dict_list

def has_all_fields(passport_dict, req_fields):
    for field in req_fields:
        if field not in passport_dict:
            return 0
    return 1

def part_one(data, req_fields):
    counter = 0
    for passport in data:
        counter += has_all_fields(passport, req_fields)
    return counter

def validate_passport(passport, check_fields):
    if not has_all_fields(passport, check_fields):
        return False
    for key in passport:
        if key == "byr":
            year = int(passport[key])
            if((year < 1920) or (year > 2002)):
                return False
        elif key == "iyr":
            year = int(passport[key])
            if((year < 2010) or (year > 2020)):
                return False
        elif key == "eyr":
            year = int(passport[key])
            if((year < 2020) or (year > 2030)):
                return False
        elif key == "hgt":
            height = passport[key]
            if("cm" not in height) and ("in" not in height):
                return False
            if "cm" in height:
                cm_height = int(height.strip("cm"))
                if((cm_height < 150) or (cm_height > 193)):
                    return False
            if "in" in height:
                in_height = int(height.strip("in"))
                if((in_height < 59) or (in_height > 76)):
                    return False
        elif key == "hcl":
            if not re.match("#[a-f0-9]{6}$",passport[key]):
                return False
        elif key == "ecl":
            if passport[key] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif key == "pid":
            if not re.match("[0-9]{9}$", passport[key]):
                return False
    return True

def part_two(data, req_fields):
    counter = 0
    for passport in data:
        if validate_passport(passport, req_fields):
            counter += 1
    return counter

nice_data = make_dict(raw_data2)
print(part_one(nice_data, check_fields))
print(part_two(nice_data, check_fields))