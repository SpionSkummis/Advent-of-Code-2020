with open("04/input04.txt", "r") as f:
#with open("04/testinput04.txt", "r") as f:
    raw_data = f.read()

split_data = raw_data.split("\n\n")

password_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
check_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def quickcheck(passport, keywords):
    for field in keywords:
        if field not in passport:
            return 0
    return 1

def checkmany(passport_db, keywords):
    counter = 0
    for passport in passport_db:
        counter += quickcheck(passport,keywords)
    return counter



print(checkmany(split_data,check_fields))
