from math import sqrt

with open("Erik/inputs/day13.txt", "r") as f:
    current_time = int(f.readline().strip())
    line2 = f.readline()
    busses_p1 = [int(x) for x in line2.strip().split(",") if x != "x"]


def is_prime(num):
    for i in range(2,round(sqrt(num)+1)):
        if (num % i) == 0:
            return False
    return True

def next_departure_time(bus_id, curr_time):
    return bus_id * ((curr_time // bus_id) + 1)

def time_to_next_departure(bus_id, curr_time):
    return next_departure_time(bus_id, curr_time) - curr_time

def part_one(bus_list, curr_time):
    saved_bus_id = curr_time ** 9
    min_wait_time = curr_time ** 9
    for bus_id in bus_list:
        curr_wait_time = time_to_next_departure(bus_id, curr_time)
        if curr_wait_time < min_wait_time:
            saved_bus_id = bus_id
            min_wait_time = curr_wait_time
    return saved_bus_id * min_wait_time

print(f"The bus ID times the time to the next departure is: {part_one(busses_p1, current_time)}")
