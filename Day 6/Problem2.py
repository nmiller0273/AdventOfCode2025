with open("./Day 6/Input.txt") as file:
    data = file.read().split("\n")

# wow, this was a tough one!
# a lot of thinking, a fair bit of eye strain later, pretty happy to ahve solved it.
# i could absolutely simplify this but its fast enough im not worried :)

for k in range(len(data)):
    data[k] = data[k].split(" ")

out = 0

operations = list(filter(None, map(str.strip, data[-1])))

nums = []
for k in range(len(data) - 1):
    i = 0
    z = 0
    numRow = []
    for _ in range(len(operations)):
        target = 0
        for j in range(z + 1, len(data[-1])):
            if data[-1][j] == "":
                target += 1
            else:
                z = j
                break
        target += 1
        row = ""
        while len(row) < target:
            row += data[k][i]
            if not data[k][i]:
                row += " "
            i += 1
        numRow.append(row)
    nums.append(numRow)

nums2 = []
for k in range(len(nums[0])):
    newRow = []
    for i in range(len(nums)):
       newRow.append(nums[i][k])
    nums2.append(newRow)

nums = []
for k in range(len(nums2)):
    newRow = []
    for j in range(len(nums2[k][0])):
        newNum = ""
        for i in range(len(nums2[k])):
            newNum += nums2[k][i][j]
        newRow.append(int(newNum))
    nums.append(newRow)

for k in range(len(nums)):
    if operations[k] == "*":
        mult = 1
        for j in nums[k]:
            mult = mult * j
        out += mult
    else:
        out += sum(nums[k])

print(out)