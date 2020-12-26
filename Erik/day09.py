raw_data = []
with open("Erik/inputs/day09.txt", "r") as f:
    for line in f:
        raw_data.append(int(line))

def is_valid(num_list, index, pre_len):
    for i in range(index-pre_len, index):
        for j in range(i+1,index):
            if num_list[i] + num_list[j] == num_list[index]:
                return True
    return False

def check_all(num_list, pre_len):
    for i in range(pre_len,len(num_list)):
        if not is_valid(num_list, i, pre_len):
            return (num_list[i])

def get_range(num_list, num):
    for i in range(len(num_list)):
        curr_sum = 0
        curr_len = 1
        while(curr_sum < num):
            curr_sum = sum(num_list[i:i+curr_len])
            curr_len += 1
        if curr_sum == num:
            return num_list[i:i+curr_len-1]

def part_two(num_list, num):
    temp_list = get_range(num_list,num)
    return min(temp_list) + max(temp_list)


failing_num = check_all(raw_data, 25)
print(f"Part 1: {failing_num}")
print(f"Part 2: {part_two(raw_data, failing_num)}")
