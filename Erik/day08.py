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

def run_code(program_list, pointer_start, acc_start):
    prog_len = len(program_list)
    acc = acc_start
    pointer = pointer_start
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

            #Failsafe, bryter om samma instruktion dyker upp
            #Kontrollera om exakt samma instruktion setts tidigare, och bryt i så fall
            if pointer in seen_instruction:
                print("Error?")
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

def run_code3(program_list, pointer_start, acc_start):
    prog_len = len(program_list)
    acc = acc_start
    pointer = pointer_start
    ended_correctly = False
    seen_instruction = set()
    while(True):
        # Check if the program has ended properly (pointer = len),
        # Else correct pointer to be within limits:
        if pointer == prog_len:
            return True, acc
        elif pointer > prog_len:
            pointer = pointer % prog_len
        elif pointer < 0:
            pointer = prog_len - pointer

        #Packa upp rätt instruktion
        instr, val = program_list[pointer]

        #Kontrollera om exakt samma instruktion setts tidigare, och bryt i så fall med felmeddelande
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
    
    # Skicka tillbaka värdet i accen
    return ended_correctly, acc




print(run_code(nice_data,0,0))

print(run_code3(nice_data,0,0))
