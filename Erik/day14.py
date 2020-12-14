import re
with open("Erik/inputs/day14-t1.txt") as f:
    raw_data = []
    for line in f:
        raw_data.append(line.strip())

def mask_int(num, mask):
    num_bin = format(num, "#038b")
    new_bin = "0b"
    for i in range(len(mask)):
        if mask[i] == "X":
            new_bin += num_bin[i+2]
        elif mask[i] == "1":
            new_bin += "1"
        elif mask[i] == "0":
            new_bin += "0"
    return int(new_bin,2)

def part_one(data_list):
    curr_mask = ""
    mem_dict = dict()
    for line in data_list:
        if line.startswith("mask"):
            curr_mask = line.split(" = ")[1]
        else:
            key, val = [int(x) for x in re.findall("[0-9]+", line)]
            mem_dict[key] = mask_int(val, curr_mask)
    
    val_sum = 0
    for key in mem_dict:
        val_sum += mem_dict[key]
    return val_sum

print(part_one(raw_data))

def get_masked_ints(num, mask):
    num_bin = format(num, "#038b")
    possible_combinations = []
    new_bin = "0b"
    for i in range(len(mask)):

        if mask[i] == "0":
            new_bin + num_bin[i+2]
        elif mask[i] == "1":
            new_bin += "1"
        elif mask[i] == "X":
            new_bin += "X"
    return new_bin

print(get_masked_ints(42, "000000000000000000000000000000X1001X"))