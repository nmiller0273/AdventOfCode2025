with open("./Day 7/Input.txt") as file:
    data = file.read().split("\n")

# this was a fun one! lots of micro-breakthroughs to make
# had to rebuild this a good couple times to account for beams as a whole rather than individually
# taking it down from memory error to near instant is very satisfying

timelines = 1
beams = dict()
for k in range(len(data[0])):
    if data[0][k] == "S":
        beams[k] = 1

for row in range(1, len(data)):
    print("Row: ", row, " out of ", len(data), timelines)
    if "^" not in data[row]:
        continue
    newBeams = []
    for beam in beams.keys():
        if data[row][beam] != "^":
            continue
        newBeams.append(beam)
        timelines += beams[beam]

    for beam in newBeams:
        beams.setdefault(beam - 1, 0)
        beams.setdefault(beam + 1, 0)
        beams[beam + 1] += beams[beam]
        beams[beam - 1] += beams[beam]
        del beams[beam]

print(beams)
print(timelines)

# 39355914187485480490374654767301498747974309079494117430937913294453657550874214400000000000 is too high