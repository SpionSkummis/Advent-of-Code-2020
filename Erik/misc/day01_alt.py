inp = []
with open("01/input01.txt", "r") as f:
#with open("01/testinput.txt", "r") as f:
    for line in f:
        inp.append(int(line.strip()))

min_num = min(inp)
inp_mod = sorted([x for x in inp if not min_num + x > 2020])

def part_one(in_list):
    for i in range(len(in_list)):
        for j in range(i+1, len(in_list)):
            if(in_list[i] + in_list[j] == 2020):
                print("Part 1: " +str(in_list[i]*in_list[j]))
                return

part_one(inp_mod)

# Part Two
two_min_num_sum = inp_mod[0] + inp_mod[1] #Veckans variabelnamn, lets go!
inp_mod2 = sorted([x for x in inp_mod if not two_min_num_sum + x > 2020])

def part_two(in_list):
    for i in range(len(in_list)):
        for j in range(i+1, len(in_list)):
            for n in range(j+1, len(in_list)):
                if(in_list[i] + in_list[j] + in_list[n] == 2020):
                    print("Part 1: " +str(in_list[i]*in_list[j]*in_list[n]))
                    return

part_two(inp_mod2)
