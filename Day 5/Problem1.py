with open("./Day 5/Input.txt") as file:
    data = file.read().split("\n")

value = data[0]
index = 0
out = 0
ranges = []
while value != "":
    points = value.split("-")
    ranges.append([int(points[0]), int(points[1]) + 1])
    index += 1
    value = data[index]

data = data[index+1:]

for k in data:
    for i, j in ranges:
        if i <= int(k) <= j:
            out += 1
            break

print(out)