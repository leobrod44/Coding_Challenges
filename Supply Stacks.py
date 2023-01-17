import numpy

file =  open('data.txt', 'r')
stacks = []
rows = []
lines = file.readlines()

directionStart = 0
for line in lines:
    directionStart+=1
    row = line.replace(" ","")
    if "1" in row:
        numCols = len(row)-1
        directionStart+=1
        break
stacks = [ [] for i in range(numCols)]

for line in lines:
    index = 0
    if "1" in line:
        row = line.replace(" ","")
        print(row)
        numCols = len(row)-1
        break
    for i in range(1, len(line), 4):
        if line[i] !=" ":
            stacks[index].append(line[i])
        index+=1

print(stacks)

directions= lines[directionStart:]
directions[-1]+="\n"

stacksReverted = []
for stack in stacks:
    stacksReverted.append(stack[::-1])
stacks = stacksReverted
print(stacks)
print(directions)
for direction in directions:
    mov = int(direction[5:direction.index("f")-1])
    fro = int(direction[direction.index("om")+2:direction.index("t")-1])-1
    to = int(direction[direction.index("to")+2:direction.index("\n")])-1
    toAdd = []
    for i in range(mov):
        print()
        if len(stacks[fro])>0:
            elem = stacks[fro].pop(-1)
            toAdd.append(elem)
        print(stacks)
    toAdd = toAdd[::-1]
    stacks[to]+=toAdd
    print(stacks)

answer = ''
for stack in stacks:
    answer += stack[-1]

print(answer)