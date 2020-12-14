with open("Erik/inputs/day11.txt", "r") as f:
	default_map = [x.strip() for x in f]

def get_adj(seats, y_pos, x_pos):
    taken_counter = 0
    y_range = [a for a in range(y_pos-1,y_pos+2) if (a >= 0 and a < len(seats))]
    x_range = [a for a in range(x_pos-1,x_pos+2) if (a >= 0 and a < len(seats[0]))]
    for y in y_range:
        for x in x_range:
            if not (x == x_pos and y == y_pos):
                if seats[y][x] == "#":
                    taken_counter += 1
    return taken_counter

def make_next_gen(start_map):
    next_map = []
    for y in range(len(start_map)):
        next_line = ""
        for x in range(len(start_map[0])):
            if start_map[y][x] == ".":
                next_line += "."
            elif start_map[y][x] == "L":
                if get_adj(start_map,y,x) == 0:
                    next_line += "#"
                else:
                    next_line += "L"
            elif start_map[y][x] == "#":
                if get_adj(start_map,y,x) >= 4:
                    next_line += "L"
                else:
                    next_line += "#"
        next_map.append(next_line)
    return next_map

def find_steady_state(start_map):
    gen_no = 0
    current_gen = start_map
    while True:
        next_gen = make_next_gen(current_gen)
        if current_gen == next_gen:
            break
        current_gen = next_gen.copy()
        gen_no += 1
    return gen_no, current_gen

def taken_seat_counter(any_map):
    taken_counter = 0
    for y in range(len(any_map)):
        for x in range(len(any_map[0])):
            if any_map[y][x] == "#":
                taken_counter += 1
    return taken_counter

gen_num, final_map = find_steady_state(default_map)
print(f"For part one, the seats stabilize at generation {gen_num}. At that time, {taken_seat_counter(final_map)} seats are taken")

def visible_dir(seats, y_pos, x_pos, y_delta, x_delta):
    y_range = range(0,len(seats))
    x_range = range(0,len(seats[0]))
    y = y_pos + y_delta
    x = x_pos + x_delta

    while (y in y_range) and (x in x_range):
        if seats[y][x] == "#":
            return 1
        elif seats[y][x] == "L":
            return 0
        y += y_delta
        x += x_delta
    return 0

def get_visible(seats, y_pos, x_pos): #Detta kan vara mitt vackraste kodblock någonsin. 5/5 spaghettistrån, skulle koka igen.
    visible_counter = 0
    visible_counter += visible_dir(seats,y_pos,x_pos,-1,-1)
    visible_counter += visible_dir(seats,y_pos,x_pos,-1,0)
    visible_counter += visible_dir(seats,y_pos,x_pos,-1,1)
    visible_counter += visible_dir(seats,y_pos,x_pos,0,-1)
    visible_counter += visible_dir(seats,y_pos,x_pos,0,1)
    visible_counter += visible_dir(seats,y_pos,x_pos,1,-1)
    visible_counter += visible_dir(seats,y_pos,x_pos,1,0)
    visible_counter += visible_dir(seats,y_pos,x_pos,1,1)
    return visible_counter

def make_next_gen2(start_map):
    next_map = []
    for y in range(len(start_map)):
        next_line = ""
        for x in range(len(start_map[0])):
            if start_map[y][x] == ".":
                next_line += "."
            elif start_map[y][x] == "L":
                if get_visible(start_map,y,x) == 0:
                    next_line += "#"
                else:
                    next_line += "L"
            elif start_map[y][x] == "#":
                if get_visible(start_map,y,x) >= 5:
                    next_line += "L"
                else:
                    next_line += "#"
        next_map.append(next_line)
    return next_map

def find_steady_state2(start_map):
    gen_no = 0
    current_gen = start_map
    while True:
        next_gen = make_next_gen2(current_gen)
        if current_gen == next_gen:
            break
        current_gen = next_gen.copy()
        gen_no += 1
    return gen_no, current_gen


gen_num2, final_map2 = find_steady_state2(default_map)
print(f"For part two, the seats stabilize at generation {gen_num2}. At that time, {taken_seat_counter(final_map2)} seats are taken")
