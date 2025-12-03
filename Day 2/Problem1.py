with open("./Day 2/ProblemOneInput.txt") as file:
    commands = file.read().split(",")
    for k in range(len(commands)):
        commands[k] = commands[k].split("-")
        commands[k][0] = int(commands[k][0])
        commands[k][1] = int(commands[k][1])


out = 0

for command in commands:
    for k in range(command[0], command[1] + 1):
        curr = str(k)
        length = len(curr)
        if length % 2 == 1:
            continue
        lengthHalf = length // 2
        fake = False
        for j in range(lengthHalf):
            if curr[j] != curr[j + lengthHalf]:
                fake = True
                break
        if fake == False:
            out += k

print(out)

#730 is too low