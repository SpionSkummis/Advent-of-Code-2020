import re, sys
sys.setrecursionlimit(2500)

# 111 too low

# ([0-9]+)([ a-z]+)
raw_data = []
#with open("Erik/inputs/day07.txt", "r") as f:
with open("Erik/inputs/day07.txt", "r") as f:
    for line in f:
        raw_data.append(line.strip())


def make_dict(raw):
    main_dict = dict()
    for line in raw:
        temp_dict = dict()
        key = line.split(" bags contain ")[0]
        vals = re.findall("([0-9]+)([ a-z]+)", line)
        if vals:
            for match in vals:
                temp_dict[match[1].rstrip("bags ").lstrip(" ")] = match[0] #Här kan det vara en idé att konvertera till int i framtiden
        main_dict[key] = temp_dict
    return main_dict

"""
def contains_gold(hueg_dict, bag):
    if "shiny gold" in 
"""

def find_gold_containers(hueg_dict, bag_colour): # Det här är helt feltänkt. Varje steg måste leta vidare. hm.
    parents = []
    for key in hueg_dict:
        if bag_colour in hueg_dict[key]:
            parents.append(key)
    for bag in parents:
        new_parents = find_gold_containers(hueg_dict,bag)
        for item in new_parents:
            parents.append(item)
    return parents

def part_one(hueg_dict, bag_colour):
    return len(set(find_gold_containers(hueg_dict,bag_colour)))

    """
    containers = []
    for key in hueg_dict:
        if contains_gold(hueg_dict[key]):
            containers.append(key)
    return containers
    """


nice_data = make_dict(raw_data)
#print(nice_data)
#print(find_gold_containers(nice_data))

"""
for key in nice_data:
    print(key, nice_data[key])
    if("faded blue" in nice_data[key]):
        print("Blå?")
    if(5 in nice_data[key]):
        print("Fem?")
"""

print(find_gold_containers(nice_data, "shiny gold"))
print(len(nice_data))
print(part_one(nice_data,"shiny gold"))



"""
def find_gold_containers(hueg_dict): # Det här är helt feltänkt. Varje steg måste leta vidare. hm.
    
    if type(hueg_dict) == str:
        if hueg_dict == "shiny gold":
            return True
        return False
    for key in hueg_dict:
        if "shiny gold" in hueg_dict[key]:
            return True
        #print(key, type(hueg_dict[key]))
        #if type(hueg_dict[key]) == dict:
        return(contains_gold(hueg_dict[key]))
            
        
        if "bright gold" in hueg_dict[key]:
            return True
        contains_gold(hueg_dict[key])
        
    return False
"""