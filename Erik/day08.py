import re

def parse_code(filename):
    parsed_list = []
    with open(filename, "r") as f:
        for line in f:
            linematch = re.match("([a-z]{3}) ([+-][0-9]+)", line)
            parsed_list.append([linematch[1], int(linematch[2])])
    return parsed_list


nice_data = parse_code("Erik/inputs/day08.txt")

#print(nice_data)

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
    loops = 0
    while(True):
        for rep in range(0,prog_len*2):
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


print(run_code(nice_data))

print(run_code2(nice_data))