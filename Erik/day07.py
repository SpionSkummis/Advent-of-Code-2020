import re

raw_data = []
with open("Erik/inputs/day07.txt","rt") as f:
    for line in f:
        raw_data.append(line.strip())

def make_contains_dict(in_data):
    main_dict = dict()
    for line in in_data:
        temp_dict = dict()
        key = line.split(" bags contain ")[0]
        vals = re.findall("([0-9]+)([ a-z]+)", line)
        if vals:
            for match in vals:
                temp_dict[match[1].rstrip("bags").strip(" ")] = int(match[0])
        main_dict[key] = temp_dict
    return main_dict

def make_appears_in_dict(in_data):
    main_dict = dict()
    colours = [x.split(" bags contain")[0] for x in in_data]
    for line in in_data:
        for col in colours:
            if col not in main_dict:
                main_dict[col] = []
            if col in line.split("bags contain ")[1]:
                main_dict[col].append(line.split(" bags contain ")[0])
    return main_dict

def get_containers(col, in_dict):
    containers = set()
    containers.update(in_dict[col])
    for cols in list(containers):
        containers.update(get_containers(cols, in_dict))
    return containers

def get_contained_bags(col, in_dict):
    bag_amount = 1
    if len(in_dict[col]) == 0:
        return bag_amount
    for key in in_dict[col]:
        temp_amount = in_dict[col][key]
        temp_amount *= get_contained_bags(key,in_dict)
        bag_amount += temp_amount
    return bag_amount
    
app_dict = make_appears_in_dict(raw_data)
poss_containers = get_containers("shiny gold", app_dict)
print(f"{len(poss_containers)} bag colours will sooner or later contain a shiny gold bag")

contains_dict = make_contains_dict(raw_data)
print(f'The shiny gold bag contains {get_contained_bags("shiny gold", contains_dict)-1} bags') #Svaret blir ett för mycket och jag förstår inte riktigt varför.
