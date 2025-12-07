with open("./Day 5/Input.txt") as file:
    data = file.read().split("\n")

# i admit, i needed help with this one! at first i had the idea explained via the subreddit and i didnt really get it,
# but after sleeping on it i got 90% of the way there. still, i needed some help get across the finish line- namely the
# max(curEnd, ranges[k][1]) point. still, this was an interesting problem!

out = 0
ranges = []

for value in data:
    if value == "":
        break
    points = value.split("-")
    ranges.append([int(points[0]), int(points[1]) + 1])

ranges = sorted(ranges, key=lambda ranges: ranges[0])

newRanges = []
curStart = ranges[0][0]
curEnd = ranges[0][1]
for k in range(1, len(ranges)):
    if ranges[k][0] > curEnd:
        newRanges.append([curStart, curEnd])
        curStart = ranges[k][0]
        curEnd = ranges[k][1]
    else:
        curEnd = max(curEnd, ranges[k][1])

if newRanges[-1] != [curStart, curEnd]:
    newRanges.append([curStart, curEnd])

for s, e in newRanges:
    out += max(0, e - s)

print(newRanges)
print(out)

# 329895650997598 is too low