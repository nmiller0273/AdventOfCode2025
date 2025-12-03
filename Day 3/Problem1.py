with open("./Day 3/ProblemOneInput.txt") as file:
    commands = file.read().split("\n")


out = 0
for command in commands:
    curr = 0
    loc = 0
    for i in range(len(command) - 1):
        if int(command[i]) > curr:
            curr = int(command[i])
            loc = i
    out += curr * 10
    curr = 0
    for j in range(loc+1, len(command)):
        if int(command[j]) > curr:
            curr = int(command[j])
    out += curr

print(out)