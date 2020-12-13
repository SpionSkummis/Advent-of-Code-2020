# Part 2 90322 too high
with open("Erik/inputs/day12.txt", "r") as f:
    instr_list = []
    for line in f:
        instr_list.append((line[0],int(line[1:])))


def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def sail_ship(instruction_list):
    heading = 90
    x_pos = 0
    y_pos = 0
    for instruction in instruction_list:
        instr_key = instruction[0]
        instr_val = instruction[1]

        if instr_key == "E" or (instr_key == "F" and heading == 90):
            x_pos += instr_val
        elif instr_key == "N" or (instr_key == "F" and heading == 0):
            y_pos += instr_val
        elif instr_key == "W" or (instr_key == "F" and heading == 270):
            x_pos -= instr_val
        elif instr_key == "S" or (instr_key == "F" and heading == 180):
            y_pos -= instr_val
        elif instr_key == "R":
            heading = (heading + instr_val) % 360
        elif instr_key == "L":
            heading = (heading - instr_val) % 360
    return [x_pos,y_pos]


final_pos = sail_ship(instr_list)
print(f"Using the first set of rules, the ship ends up at {final_pos[0]}, {final_pos[1]}.\nThat is {manhattan(final_pos[0],final_pos[1],0,0)} steps from the starting position.\n")


def rotate_waypoint(key, val, x, y):
    if val == 0:
        return x, y
    elif val == 180:
        return x*-1, y*-1
    elif (key == "R" and val == 90) or (key == "L" and val == 270):
        return y, x*-1
    elif (key == "L" and val == 90) or (key == "R" and val == 270):
        return y*-1, x
    else:
        print("ERROR!")
        return 0,0


def sail_ship2(instruction_list):
    ship_x = 0
    ship_y = 0
    way_x = 10
    way_y = 1

    for instruction in instruction_list:
        instr_key = instruction[0]
        instr_val = instruction[1]

        if(instr_key == "F"):
            ship_x += (way_x * instr_val)
            ship_y += (way_y * instr_val)

        elif(instr_key == "E"):
            way_x += instr_val
        elif(instr_key == "N"):
            way_y += instr_val
        elif(instr_key == "W"):
            way_x -= instr_val
        elif(instr_key == "S"):
            way_y -= instr_val

        else:
            way_x, way_y = rotate_waypoint(instr_key, instr_val, way_x, way_y)

    return [ship_x, ship_y]


final_pos2 = sail_ship2(instr_list)
print(f"Using the second set of rules, the ship ends up at {final_pos2[0]}, {final_pos2[1]}.\nThat is {manhattan(final_pos2[0],final_pos2[1],0,0)} steps from the starting position.")
