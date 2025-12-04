with open("./Day 4/ProblemOneInput.txt") as file:
    layout = file.read().split("\n")

# another fairly easy one today-
# i feel like ive done enough similar problems i could do this under a timer!

length = len(layout)
height = len(layout[0])
out = 0
directions = ((0, 1), (1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1))

def checkNeighbours(x, y, d):
    toCheck = []
    for direction in d:
        toCheck.append([x + direction[0], y + direction[1]])

    invalidNeighbours = 0
    for check in toCheck:
        if check[0] < 0 or check[1] < 0:
            continue
        if check[0] >= length or check[1] >= height:
            continue
        if layout[check[0]][check[1]] == "@":
            invalidNeighbours += 1
    return invalidNeighbours

stored = 0
while True:
    for row in range(length):
        for column in range(height):
            if layout[row][column] == "@":
                if checkNeighbours(row, column, directions) < 4:
                    out += 1
                    layout[row] = layout[row][:column] + "." + layout[row][column + 1:]
    if out == stored:
        break
    stored = out

print(out)