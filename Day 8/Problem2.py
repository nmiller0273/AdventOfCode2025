with open("./Day 8/Input.txt") as file:
    data = file.read().split("\n")

# more than actually being hard, this one terrified me!
# turns out to actually be a far simpler problem than i realised, had a good time with it once i realised what i was doing

for i in range(len(data)):
    data[i] = data[i].split(",")
    for k in range(len(data[i])):
        data[i][k] = int(data[i][k])

def getDistance(coords1, coords2):
    total = 0
    for i in range(len(coords1)):
        total += (max(coords1[i], coords2[i]) - min(coords1[i], coords2[i])) ** 2
    
    return total

all = set()
allPoints = set()

for i in range(len(data)-1):
    allPoints.add(i)
    for j in range(i+1, len(data)):
        curr = getDistance(data[i], data[j])
        all.add((curr, (i, j)))

allPoints.add(len(data)-1)
        
all = list(all)
all.sort()

for line in all:
    allPoints.discard(line[1][0])
    allPoints.discard(line[1][1])
    if len(allPoints) == 0:
        out = 1
        out = out * data[line[1][1]][0] * data[line[1][0]][0]
        break

print(out)