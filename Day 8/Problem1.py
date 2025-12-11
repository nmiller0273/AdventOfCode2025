import math

with open("./Day 8/Input.txt") as file:
    data = file.read().split("\n")

for i in range(len(data)):
    data[i] = data[i].split(",")
    for k in range(len(data[i])):
        data[i][k] = int(data[i][k])

def getDistance(coords1, coords2):
    total = 0
    for i in range(len(coords1)):
        total += (max(coords1[i], coords2[i]) - min(coords1[i], coords2[i])) ** 2

    total = math.sqrt(total)
    
    return total

threshold = (math.inf, (0, 0))
best = set()
best.add(threshold)
size = 1000


for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        curr = getDistance(data[i], data[j])
        if curr < threshold[0]:
            best.add((curr, (i, j)))
            if len(best) > size:
                best.remove(threshold)
                threshold = max(best, key = lambda t: t[0])

print(best)

seen = set()
circuits = { 0 : [] }
circuitId = 1
for k in best:
    i, j = k[1]
    if i not in seen and j not in seen:
        seen.add(i)
        seen.add(j)
        circuits[circuitId] = [i, j]
        circuitId += 1
    else:
        seen.add(i)
        seen.add(j)
        iCurcuit = -1
        jCurcuit = -1
        for circuit in circuits.keys():
            if i in circuits[circuit]:
                iCurcuit = circuit
            if j in circuits[circuit]:
                jCurcuit = circuit
            if iCurcuit != -1 and jCurcuit != -1:
                break
        if iCurcuit == jCurcuit:
            continue

        elif iCurcuit != jCurcuit and iCurcuit != -1 and jCurcuit != -1:
            circuits[iCurcuit] = circuits[iCurcuit] + circuits[jCurcuit]
            del circuits[jCurcuit]

        elif iCurcuit == -1 and jCurcuit != -1:
            circuits[jCurcuit].append(i)

        elif iCurcuit != -1 and jCurcuit == -1:
            circuits[iCurcuit].append(j)
        
        else:
            print("oops all errors")
            print(i, j, iCurcuit, jCurcuit)
            print(circuits)

longestThree = [1, 1, 1]
minNum = 1

for circuit in circuits.keys():
    if len(circuits[circuit]) > minNum:
        longestThree.append(len(circuits[circuit]))
        longestThree.remove(minNum)
        minNum = min(longestThree)

print(seen)
print(circuits)
print(longestThree)
print(longestThree[0] * longestThree[1] * longestThree[2])