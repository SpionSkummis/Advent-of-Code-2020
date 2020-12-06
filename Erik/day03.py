my_map = []

with open("Erik/inputs/day03.txt", "r") as f:
#with open("Erik/inputs/day03-t1", "r") as f:
    for line in f:
        my_map.append(line.strip())

def is_pos_a_tree(pos_x, pos_y, grid_map):
    if pos_x >= len(grid_map[0]):
        pos_x = pos_x % len(grid_map[0])
    if grid_map[pos_y][pos_x] == "#":
        return 1
    return 0

def collision_counter(x_step, y_step, grid_map):
    col_count = 0
    x = 0
    y = 0
    while y < len(grid_map):
        col_count += is_pos_a_tree(x,y,grid_map)
        x += x_step
        y += y_step
    return col_count

def part_two(instructions, grid_map):
    part_two_ans = 1
    for instr in instructions:
        part_two_ans *= collision_counter(instr[0],instr[1],grid_map)
    return part_two_ans


print(f"In part one, {collision_counter(3,1,my_map)} trees would be hit")

part_two_ratios = ((1,1),(3,1),(5,1),(7,1),(1,2))
print(f"The product of the numbers of trees hit using the 5 specified directions is: {part_two(part_two_ratios,my_map)}")
