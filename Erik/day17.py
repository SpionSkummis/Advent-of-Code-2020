def get_data_set(filename):
    active_set = set()
    with open(filename, "rt") as f:
        raw = f.read().strip().split("\n")
        for x in range(len(raw)):
            for y in range(len(raw[0])):
                if(raw[x][y] == "#"):
                    active_set.add((x,y,0))
    return active_set

def get_ranges(inset):
    x = set()
    y = set()
    z = set()
    for element in inset:
        x.add(element[0])
        y.add(element[1])
        z.add(element[2])
    return range(min(x)-1,max(x)+2), range(min(y)-1,max(y)+2), range(min(z)-1,max(z)+2)

def get_adj(coord, inset):
    counter = 0
    for x in range(coord[0]-1,coord[0]+2):
        for y in range(coord[1]-1,coord[1]+2):
            for z in range(coord[2]-1,coord[2]+2):
                if (x,y,z) in inset and coord != (x,y,z):
                    counter += 1
    return counter

def get_next_gen_set(startset):
    x_range, y_range, z_range = get_ranges(startset)
    next_gen = set()

    for x in x_range:
        for y in y_range:
            for z in z_range:
                if (x,y,z) in startset:
                    adj = get_adj((x,y,z), startset)
                    if adj == 2 or adj == 3:
                        next_gen.add((x,y,z))
                else:
                    adj = get_adj((x,y,z), startset)
                    if adj == 3:
                        next_gen.add((x,y,z))
    return next_gen

def part_one(startset, generations):
    next_gen = startset
    for _ in range(generations):
        next_gen = get_next_gen_set(next_gen)
    return len(next_gen)
#print(get_data_dict("Erik/inputs/day17-t1.txt"))
#print(get_data_set("Erik/inputs/day17-t1.txt"))

start_set = get_data_set("Erik/inputs/day17.txt")
#print(get_next_gen_set(start_set))
print(part_one(start_set,6))
"""
If a cube is active and exactly 2 or 3 of its neighbors are also active,
    the cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
    Otherwise, the cube remains inactive.
"""


def get_data_set_4d(filename):
    active_set = set()
    with open(filename, "rt") as f:
        raw = f.read().strip().split("\n")
        for x in range(len(raw)):
            for y in range(len(raw[0])):
                if(raw[x][y] == "#"):
                    active_set.add((x,y,0,0))
    return active_set

def get_ranges_4d(inset):
    x = set()
    y = set()
    z = set()
    w = set()
    for element in inset:
        x.add(element[0])
        y.add(element[1])
        z.add(element[2])
        w.add(element[3])
    return range(min(x)-1,max(x)+2), range(min(y)-1,max(y)+2), range(min(z)-1,max(z)+2), range(min(w)-1,max(w)+2)

def get_adj_4d(coord, inset):
    counter = 0
    for x in range(coord[0]-1,coord[0]+2):
        for y in range(coord[1]-1,coord[1]+2):
            for z in range(coord[2]-1,coord[2]+2):
                for w in range(coord[3]-1,coord[3]+2):
                    if (x,y,z,w) in inset and coord != (x,y,z,w):
                        counter += 1
    return counter

def get_next_gen_set(startset):
    x_range, y_range, z_range, w_range = get_ranges_4d(startset)
    next_gen = set()

    for x in x_range:
        for y in y_range:
            for z in z_range:
                for w in w_range:
                    if (x,y,z,w) in startset:
                        adj = get_adj_4d((x,y,z,w), startset)
                        if adj == 2 or adj == 3:
                            next_gen.add((x,y,z,w))
                    else:
                        adj = get_adj_4d((x,y,z,w), startset)
                        if adj == 3:
                            next_gen.add((x,y,z,w))
    return next_gen

def part_two(startset, generations):
    next_gen = startset
    for _ in range(generations):
        next_gen = get_next_gen_set(next_gen)
    return len(next_gen)


p2 = get_data_set_4d("Erik/inputs/day17.txt")
print(part_two(p2,6))
