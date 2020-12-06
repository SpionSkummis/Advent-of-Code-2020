"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

test_data = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]
raw_data = []

with open("Erik/inputs/day02.txt", "r") as f:
    for line in f:
        raw_data.append(line.strip())

def parse_data(raw_list):
    nice_data = []
    for line in raw_list:
        password = line.split(": ")[1]
        find_letter = line.split(": ")[0].split(" ")[1]
        low_number = int(line.split(": ")[0].split(" ")[0].split("-")[0])
        high_number = int(line.split(": ")[0].split(" ")[0].split("-")[1])
        nice_data.append([low_number, high_number, find_letter, password])
    return nice_data

def count_letter(letter, word):
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    return counter

def part_one(nice_data):
    counter = 0
    for line in nice_data:
        n = count_letter(line[2], line[3])
        if((n <= line[1]) and (n >= line[0])):
            counter += 1
    return counter

def part_two(nice_data):
    counter = 0
    for line in nice_data:
        if(line[3][(line[0]-1)] == line[2]) != (line[3][(line[1]-1)] == line[2]):
            counter +=1 
    return counter

#parsed_test = parse_data(test_data)
#print(part_one(parsed_test), "test passwords")
#print(part_two(parsed_test), "part 2 test passwords")

work_data = parse_data(raw_data)
print(part_one(work_data), "passwords conforming to the rules.")
print(part_two(work_data), "passwords conforming to the new rules")
