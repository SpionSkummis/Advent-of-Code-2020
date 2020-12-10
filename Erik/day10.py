jolt_data = []

with open("Erik/inputs/day10.txt", "r") as f:
	jolt_data = [int(x) for x in f]

#Add the extra numbers:
jolt_temp = jolt_data
jolt_temp.append(0)
jolt_temp.append(max(jolt_data)+3)
jolt_sorted = sorted(jolt_temp)


jump_dict = dict()

for i in range(1,4):
	jump_dict[i] = 0

for i in range(1,len(jolt_sorted)):
    jump_dict[(jolt_sorted[i] - jolt_sorted[i-1])] += 1

#print(jump_dict)
print(f"The answer to part one is: {jump_dict[1] * jump_dict[3]}")





def split_groups(sort_list):
    split_lists = []
    last_break = 0
    for i in range(0,len(sort_list)):
        if (sort_list[i] - sort_list[i-1]) == 3:
            split_lists.append(sort_list[last_break:i])
            last_break = i
    return split_lists

def find_combinations(small_list):
    if len(small_list) == 0:
        print("Error")
        return 0
    elif len(small_list) == 1:
        return 1
    elif len(small_list) == 2:
        return 1
    elif len(small_list) == 3:
        return 2
    elif len(small_list) == 4:
        return 4
    elif len(small_list) == 5:
        return 7
    elif len(small_list) == 6:
        return 13
    else:
        print("Too long list, calculate moar!")
        return 0


def get_total_combinations(in_list):
    combinations = 1
    split_list = split_groups(in_list)
    for li in split_list:
        combinations *= find_combinations(li)
    return combinations

print(f"The answer to part two is: {get_total_combinations(jolt_sorted)}")
#print(split_groups(jolt_sorted))