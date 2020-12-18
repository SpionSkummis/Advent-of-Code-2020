inp_data = [0,5,4,1,10,14,7]
inp_test_data = [[0,3,6], [1,3,2], [2,1,3], [1,2,3], [2,3,1], [3,2,1], [3,1,2]]



def play_game_old(start_numbers, final_turn):

    memory_num = dict()
    round_nr = 1
    for i in range(len(start_numbers)-1):
        last_spoken = start_numbers[i]
        memory_num[last_spoken] = round_nr
        print(memory_num)
        print("Turn",round_nr,"Spoken;", last_spoken)
        round_nr += 1
    last_spoken = start_numbers[-1]
    round_nr += 1

    while(round_nr <= final_turn):
    
        if last_spoken not in memory_num:
            print("Start av ny siffra, det är runda:", round_nr,"och det senaste som sades var:", last_spoken)
            memory_num[last_spoken] = round_nr
            last_spoken = 0
            print("Slut på ny, det som sades var", last_spoken)
        else:
            print("Start av befintlig, Det är runda:", round_nr, "och det senaste som sades var",last_spoken, "som tidigare nämndes runda", memory_num[last_spoken])    
            last_spoken = round_nr - memory_num[last_spoken]
            memory_num[last_spoken] = round_nr
            print("Slut på befintlig, det som sades var", last_spoken)
        round_nr += 1
    return last_spoken

def play_game(start_numbers, final_turn):

    memory_num = dict()
    round_nr = 0
    for i in range(len(start_numbers)-1):
        round_nr += 1
        last_spoken = start_numbers[i]
        memory_num[last_spoken] = round_nr
        print(f"It is round {round_nr}. I say \"{last_spoken}\". It is a startning nr. Round value is: {memory_num[last_spoken]}")
    
    round_nr += 1
    last_spoken = start_numbers[-1]
    print(f"It is round {round_nr}. I say \"{last_spoken}\". It is a startning nr. Round value is not yet saved")

    while(round_nr <= final_turn):
        round_nr += 1
        if last_spoken not in memory_num:
            memory_num[last_spoken] = round_nr
            last_spoken = 0
            print(f"It is round {round_nr}. I say \"{last_spoken}\", because the previous number is new. Round val of previous is : {memory_num[last_spoken]}")



    last_spoken = start_numbers[-1]
    round_nr += 1



print(play_game(inp_test_data[0],10))