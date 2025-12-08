with open("./Day 6/Input.txt") as file:
    data = file.read().split("\n")

for k in range(len(data)):
    data[k] = data[k].split(" ")
    data[k] = list(filter(None, map(str.strip, data[k])))

out = 0

for k in range(len(data[0])):
    nums = []
    for i in range(len(data) - 1):
        nums.append(int(data[i][k]))
    if data[-1][k] == "+":
        out += sum(nums)
    else:
        val = 1
        for num in nums:
            val = val * num
        out += val

print(out)