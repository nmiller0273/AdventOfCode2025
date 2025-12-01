with open("./Day 1/ProblemOneInput.txt") as file:
    commands = file.read().split("\n")

"""
Fun little problem! Took me an embatessing ammount of time to 
if pos == 100, pos = 0
definitely better ways to do it, but im trying not to be a perfectinist about these things
checking the previous number was a zero also took me a good bit
"""

out = 0
pos = 50
prevPosZero = False
for command in commands:

    toAdd = int(command[1:])

    while toAdd > 100:
        toAdd -= 100
        out += 1
    if command[0] == "R":

        pos += toAdd
    else:
        pos -= toAdd

    if pos == 100:
        pos = 0

    if pos == 0:
        out += 1
        prevPosZero = True
        continue

    if pos < 0:
        pos += 100
        if prevPosZero != True:
            out += 1
    elif pos > 99:
        pos -= 100
        out += 1

    if prevPosZero == True:
        prevPosZero = False

print(out)