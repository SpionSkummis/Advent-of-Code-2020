with open("Erik/inputs/day06.txt", "r") as f:
#with open("Erik/inputs/day06-t1.txt", "r") as f:
    raw_data = f.read()
    all_groups = raw_data.strip().split("\n\n")
    for i in range(0,len(all_groups)):
        all_groups[i] = all_groups[i].split("\n")

def make_group_set(group):
    ans_set = set()
    for passenger in group:
        ans_set.update(set(passenger))
    return ans_set

def get_num_of_ans(group):
    return len(make_group_set(group))

def get_total_sum(group_list):
    total_sum = 0
    for group in group_list:
        total_sum += get_num_of_ans(group)
    return total_sum

print(f"The answer to part one is: {get_total_sum(all_groups)}")

def get_common_answers(group):
    common_ans = set(group[0])
    for i in range(1,len(group)):
        common_ans.intersection_update(set(group[i]))
    return common_ans

def get_num_of_common_ans(group):
    return len(get_common_answers(group))

def get_total_sum_2(group_list):
    total_sum = 0
    for group in group_list:
        total_sum += get_num_of_common_ans(group)
    return total_sum

print(f"The answer to part two is: {get_total_sum_2(all_groups)}")
