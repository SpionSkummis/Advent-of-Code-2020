import re
with open("Erik/inputs/day16-t2.txt", "rt") as f:
    raw_data = f.read().split("\n\n")

def get_data_fields(raw_data):
    data_fields = dict()
    split_data = raw_data[0].split("\n")
    for line in split_data:
        key = re.match("[a-z]+", line)[0]
        data_fields[key] = set()

        numbers = [int(x) for x in re.findall("[0-9]+", line)]
        for i in range(0,len(numbers), 2):
            for j in range(numbers[i],numbers[i+1]+1):
                data_fields[key].add(j)

    return data_fields

def get_own_ticket(raw_data):
    return [int(x) for x in raw_data[1].split("\n")[1].split(",")]

def get_nearby_tickets(raw_data):
    tickets = raw_data[2].strip().split("\n")[1:]
    return [[int(y) for y in x.split(",")] for x in tickets]

def check_ticket(ticket, fields):
    valid_fields = set()
    for key in fields:
        valid_fields.update(fields[key])

    invalid_nums = []
    for num in ticket:
        if num not in valid_fields:
            invalid_nums.append(num)
    return invalid_nums

def part_one(raw_data):
    data_fields = get_data_fields(raw_data)
    near_tickets = get_nearby_tickets(raw_data)

    scanning_error_rate = 0
    for ticket in near_tickets:
        scanning_error_rate += sum(check_ticket(ticket, data_fields))
    return scanning_error_rate

def get_vaild_tickets(raw_data):
    data_fields = get_data_fields(raw_data)
    near_tickets = get_nearby_tickets(raw_data)

    valid_tickets = []
    for ticket in near_tickets:
        if sum(check_ticket(ticket, data_fields)) == 0:
            valid_tickets.append(ticket)
    return valid_tickets

def part_two(raw_data):
    valid_tickets = get_vaild_tickets(raw_data)
    my_ticket = get_own_ticket(raw_data)
    data_fields = get_data_fields(raw_data)

    possible_labels = dict()
    for ticket in valid_tickets:
        for num in ticket:
            for key in data_fields:
                if num in data_fields[key]:
                    if num not in possible_labels:
                        possible_labels[num] = []
                    possible_labels[num].append(key)
    print(my_ticket, possible_labels)
    own_keys = dict()
    for num in my_ticket:
        own_keys[num] = set()
        for key in possible_labels:
            if num == key:
                print("working")
                for n in possible_labels[key]:
                    own_keys[num].add(n)
        
    print("hej",own_keys)


    #print(possible_labels)
print(part_one(raw_data))

print(part_two(raw_data))