# 3607989 too high

raw_data = []
with open("Erik/inputs/day09-t1.txt", "r") as f:
    for line in f:
        raw_data.append(int(line))

#print(raw_data)

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

failing_num = check_all(raw_data, 5)
print(failing_num)

def get_range(num_list, num):
    for i in range(len(num_list)):
        curr_sum = 0
        curr_len = 1
        while(curr_sum < num):
            curr_sum = sum(num_list[i:i+curr_len])
            curr_len += 1
            print(curr_sum, curr_len, i)
        if curr_sum == num:
            return num_list[i:i+curr_len]
            

def part_two(num_list, num):
    temp_list = get_range(num_list,num)
    print(temp_list[0], temp_list[-1])
    return temp_list[0] + temp_list[-1]
    
print(part_two(raw_data, failing_num))