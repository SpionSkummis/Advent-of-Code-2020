test_data = [5764801,17807724]
main_data = [int(x) for x in open("Erik/inputs/day25.txt", "rt")]

def run_rounds(subj_num, rounds):
    res = 1
    for _ in range(rounds):
        res = (res * subj_num) % 20201227
    return res

def find_rounds(pub_key, subj_num):
    rounds = 0
    curr_num = 1
    while(True):
        rounds += 1
        curr_num = (curr_num * subj_num) % 20201227
        if curr_num == pub_key:
            return rounds

def find_enc_key(in_list):
    rounds = [find_rounds(x,7) for x in in_list]
    keys = [run_rounds(in_list[0],rounds[1]), run_rounds(in_list[1],rounds[0])]
    return keys

if find_enc_key(test_data) == [14897079,14897079]:
    print("Running test case... PASS")
    print(f"The encryption key is: {find_enc_key(main_data)[0]}")
else:
    print("Test case FAILED. Rewrite everything")
