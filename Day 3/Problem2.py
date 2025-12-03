with open("./Day 3/ProblemOneInput.txt") as file:
    commands = file.read().split("\n")


# this first problem is a pretty simple one ive done dozens of time, so i tried to do it a little different than i normally would
# but i liked this second question this was unique and neat

out = 0
for command in commands:
    curr = 0
    loc = -1
    digit = 11
    while digit != -1:
        for i in range(loc + 1, len(command) - digit):
            if int(command[i]) > curr:
                curr = int(command[i])
                loc = i
        out += curr * (10 ** digit)
        digit -= 1
        curr = 0

print(out)