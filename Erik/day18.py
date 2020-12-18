import re
def get_input(filename):
    instr_list = []
    with open(filename, "rt") as f:
        for line in f:
            instr_list.append(line.strip().replace(" ", ""))
    return instr_list

def eval_eq(eq_str):
    ans = eq_str[0]
    for i in range(1,len(eq_str)):
        if eq_str == "+":
            pass
        if eq_str == "*":
            pass
        if eq_str == "(":
            pass
    pass
def eval_eq2(eq_str):
    parentesis = re.findall("\(([^()]|(?R))*\)", eq_str)
    if not parentesis:
        print("Hej")
p1 = get_input("Erik/inputs/day18-t1.txt")
print(p1)
eval_eq2(p1[0])


