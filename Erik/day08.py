import re, copy

def parse_code(filename):
    parsed_list = []
    with open(filename, "rt") as f:
        for line in f:
            linematch = re.match("([a-z]{3}) ([+-][0-9]+)", line)
            parsed_list.append([linematch[1], int(linematch[2])])
    return parsed_list

def run_code(program_list):
    prog_len = len(program_list)
    acc = 0
    pointer = 0
    seen_instruction = set()
    while(True):
        #Check pointer to be within limits:
        if pointer > prog_len:
            pointer = pointer % prog_len
        elif pointer < 0:
            pointer = prog_len - pointer

        #Packa upp rätt instruktion
        instr, val = program_list[pointer]

        #Kontrollera om exakt samma instruktion setts tidigare, och bryt i så fall
        if pointer in seen_instruction:
            break
        seen_instruction.add(pointer)

        #Kör koden
        if instr == "nop":
            pointer += 1
        elif instr == "acc":
            acc += val
            pointer += 1
        elif instr == "jmp":
            pointer += val
    
    # Skicka tillbaka värdet i accen
    return acc

def run_code2(program_list):
    prog_len = len(program_list)
    acc = 0
    pointer = 0
    seen_instruction = set()
    while(True):
        #Check pointer to be within limits, and see if the program has ended in a correct fashion:
        #if pointer == prog_len or pointer == -1 or (pointer % prog_len) == prog_len:
        if pointer > prog_len:
            pointer = pointer % prog_len
        elif pointer < 0:
            pointer = prog_len - pointer
        if pointer == prog_len:
            return True, acc

        #Packa upp rätt instruktion
        instr, val = program_list[pointer]

        #Kontrollera om exakt samma instruktion setts tidigare, och bryt i så fall
        if pointer in seen_instruction:
            return False, acc
        seen_instruction.add(pointer)

        #Kör koden
        if instr == "nop":
            pointer += 1
        elif instr == "acc":
            acc += val
            pointer += 1
        elif instr == "jmp":
            pointer += val

def part_two(program_list):
    all_programs = []
    for _ in range(len(program_list)):
        all_programs.append(copy.deepcopy(program_list))
    for i in range(len(all_programs[0])):
        if all_programs[i][i][0] == "jmp":
            all_programs[i][i][0] = "nop"
        elif all_programs[i][i][0] == "nop":
            all_programs[i][i][0] = "jmp"

    for prog in all_programs:
        corr, acc = run_code2(prog)
        if corr:
            return acc
    return "No correct soloution found :("


nice_data = parse_code("Erik/inputs/day08.txt")
print(run_code(nice_data))
print(part_two(nice_data))
