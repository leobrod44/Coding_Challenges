import numpy

file =  open('data.txt', 'r')
f = file.readlines()
elves = []
currentElf = []
for line in f:
    if line =='\n' or line == f[-1]:
        elves.append(currentElf)
        currentElf=[]
    else:
        line = line.strip("\n")
        currentElf.append(line)
 


maxElfs = [0,0,0]


for elf in elves:
    elfTot = 0
    for data in elf:
        elfTot+=int(data)
    
    if len(maxElfs) == 0:
        maxElfs.insert(0, elfTot)
    for i in range(3):
        if elfTot>maxElfs[i]:
            if i == 0:
                maxElfs[0]= elfTot
            if i == 1:
                maxElfs[0]= maxElfs[1]
                maxElfs[1]= elfTot
            if i == 2:
                maxElfs[0]=maxElfs[1]
                maxElfs[1]= maxElfs[2]
                maxElfs[2]= elfTot

print(1)
print(maxElfs[-1]+maxElfs[-2]+maxElfs[-3])
