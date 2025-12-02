with open("./Day 2/ProblemTwoInput.txt") as file:
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
        fake = False

        for i in range(1, ((length // 2) + 1)):
            fake = False
            if length % i != 0:
                continue

            for j in range(i, length):
                if curr[j] != curr[j - i]:
                    fake = True
                    break
                
            if fake == False:
                out += k
                break


print(out)