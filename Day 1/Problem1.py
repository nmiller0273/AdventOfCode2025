with open("./Day 1/ProblemOneInput.txt") as file:
    commands = file.read().split("\n")

out = 0
pos = 50
for command in commands:
    if command[0] == "R":
        pos += int(command[1:])
    else:
        pos -= int(command[1:])
    pos = pos % 100
    if pos == 0:
        out += 1
    elif pos < 0:
        pos += 100

print(out)