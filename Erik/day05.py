
all_passes = []
with open("Erik/inputs/day05.txt", "r") as f:
#with open("Advent-of-Code-2020/Erik/inputs/day04-t1.txt", "r") as f:
    for line in f:
        all_passes.append(line.strip())

def get_x(boarding_pass):
    bin_str = "0b" + boarding_pass[0:7].replace("F","0").replace("B","1")
    return int(bin_str, 2)

def get_y(boarding_pass):
    bin_str = "0b" + boarding_pass[7:].replace("L","0").replace("R","1")
    return int(bin_str, 2)

def part_one(boarding_pass_list):
    max_id = -1
    for boarding_pass in boarding_pass_list:
        seat_id = get_x(boarding_pass)* 8 + get_y(boarding_pass)
        if seat_id > max_id:
            max_id = seat_id
    return max_id

def get_seat_pos(boarding_pass):
    return (get_x(boarding_pass),get_y(boarding_pass))

"""
#testcases:
print(get_x("FBFBBFFRLR"), get_y("FBFBBFFRLR"))
print(part_one(["FBFBBFFRLR"]))
print(get_seat_pos("FBFBBFFRLR"))
"""
print(f"The hightest seat ID is: {part_one(all_passes)}")

def get_possible_seats(boarding_pass_list):
    all_seats_set = set()
    for x in range(0,128):
        for y in range(0,8):
            all_seats_set.add((x,y))
    all_taken_set = set()
    for boarding_pass in boarding_pass_list:
        all_taken_set.add(get_seat_pos(boarding_pass))
    diff_set = all_seats_set.difference(all_taken_set)
    for i in range(0,128):
        whole_row = [x for x in diff_set if x[0] == i]
        if len(whole_row) == 8:
            diff_set.difference_update(whole_row)
    return diff_set

def get_seat(boarding_pass_list):
    all_seats_set = set()
    for x in range(0,128):
        for y in range(0,8):
            all_seats_set.add((x,y))
    all_taken_set = set()
    for boarding_pass in boarding_pass_list:
        all_taken_set.add(get_seat_pos(boarding_pass))
    diff_set = all_seats_set.difference(all_taken_set)
    for i in range(0,128):
        free_seats_in_row = [x for x in diff_set if x[0] == i]
        if len(free_seats_in_row) == 1:
            return(free_seats_in_row)
    return "Not working properly"

my_seat = get_seat(all_passes)
print(f"Your seat is located at row {my_seat[0][0]} column {my_seat[0][1]}, with a seat ID of {my_seat[0][0]*8+my_seat[0][1]}")
