import os

inp = []
with open("Advent-of-Code-2020/Erik/inputs/day01.txt", "r") as f:
#with open("Advent-of-Code-2020/Erik/inputs/day01-t1.txt", "r") as f:
    for line in f:
        inp.append(int(line.strip()))

# Part One
numA = 0
numB = 0
for i in range(len(inp)):
    for j in range(i+1, len(inp)):
        if((inp[i]+inp[j]) == 2020):
            numA = inp[i]
            numB = inp[j]
            print(numA, numB, (numA * numB))
            break
    if(numA > 0):
        break


# Part Two
numA = 0
numB = 0
numC = 0
for i in range(len(inp)):
    for j in range(i+1, len(inp)):
        for n in range(j+1, len(inp)):
            if((inp[i]+inp[j]+inp[n]) == 2020):
                numA = inp[i]
                numB = inp[j]
                numC = inp[n]
                print(numA, numB, numC, (numA * numB * numC))
                break
        if(numA > 0):
            break
    if(numA > 0):
        break

