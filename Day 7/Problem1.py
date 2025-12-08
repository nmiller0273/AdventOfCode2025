with open("./Day 7/Input.txt") as file:
    data = file.read().split("\n")

splits = 0
beams = set()
for k in range(len(data[0])):
    if data[0][k] == "S":
        beams.add(k)

for row in range(len(data)):
    newBeams = set()
    for beam in beams:
        if data[row][beam] != "^":
            continue
        splits += 1
        newBeams.add(beam)

    for beam in newBeams:
        beams.add(beam - 1)
        beams.add(beam + 1)
        beams.remove(beam)

print(beams)
print(splits)