file =  open('directions.txt', 'r')
f = file.readlines()
coords = []
folds = []
next = False
count = 0
for line in f:
    if line == "\n":
        next = True
    if next == False:
        trait = line.index(",")
        coords.append((int(line[:trait]), int(line[trait+1:].strip("\n"))))
    else:
        trait = 11
        folds.append((line[trait:].strip('\n')))
        count+=1
        # if count ==2:
        #     break
folds.remove('')
print(coords)
print(folds)
maxX = 0
maxY = 0
x =[]
y = []
for c in coords:
    x.append(c[0])
    y.append(c[1])
    if c[1]>maxX:
        maxX = c[1]
    if c[0]>maxY:
        maxY = c[0]

#store
paper = []
for i in range(maxX+1):
    current = []
    for j in range(maxY+1):
        if (j,i) not in coords:  
            current.append(".")
        else:
            current.append("#")
    paper.append(current)

for command in folds:
    part1 = []
    part2 = []
    if command[0] =="x":
        for i in range(len(paper)):
            row = []
            for j in range(0,int(command[2:])):
                row.append(paper[i][j])
            part1.append(row)
        for i in range(len(paper)):
            row = []
            for j in range(int(command[2:])+1,len(paper[0])):
                row.append(paper[i][j])
            part2.append(row)
        flipped =[]
        for i in range(len(part2)):
            row = []
            for c in range(len(part2[0])-1,-1,-1):
                row.append(part2[i][c])
            flipped.append(row)
        for i in range(len(flipped)):
            for j in range(len(flipped[0])):
                if flipped[i][j] =="#":
                    part1[i][j] ="#"
        paper = part1

    if command[0] =="y":
        for i in range(0,int(command[2:])):
            row = []
            for j in range(len(paper[0])):
                row.append(paper[i][j])
            part1.append(row)
        for i in range(int(command[2:])+1,len(paper)):
            row = []
            for j in range(len(paper[0])):
                row.append(paper[i][j])
            part2.append(row)
        flipped =[]
        for c in range(len(part2)-1,-1,-1):
            flipped.append(part2[c])

        for i in range(len(flipped)):
            for j in range(len(flipped[0])):
                if flipped[i][j] =="#":
                    part1[i][j] ="#"
        paper = part1

holeCount = 0
for row in paper:
    for i in row:
        print(i,end = " ")
    print()
print(*paper , sep = "\n")
for row in paper:
    for col in row:
        if col =="#":
            holeCount+=1
print(holeCount)
    