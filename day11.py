file =  open('directions.txt', 'r')
f = file.readlines()
global grid
grid = []
for line in f:
    line =line.strip("\n")
    numLine = []
    for c in line:
        numLine.append(int(c))
    grid.append(numLine)



# def checkFlash():
#     for row in range(len(grid)):
#         for col in range(len(grid[0])):
#             if grid[row][col]>9:
#                 isIn = False
#                 for f in flashed:
#                     if f[0]==row and f[1]==col:
#                         isIn = True
#                 if isIn == False:
#                     toFlash.append((row,col))
#                     flash(row,col)


tempFlashCount=0
def flash(i,j, toFlash, flashed):
    global flashcount
    global tempFlashCount
    tempFlashCount+=1
    flashcount+=1
    ticked =[]
    if i+1<len(grid):
        grid[i+1][j]+=1
        ticked.append((i+1,j))
        if j+1<len(grid[0]):
            grid[i+1][j+1]+=1
            ticked.append((i+1,j+1))
        if j-1>=0:
            grid[i+1][j-1]+=1
            ticked.append((i+1,j-1))
    if i-1>=0:
        grid[i-1][j]+=1
        ticked.append((i-1,j))
        if j+1<len(grid[0]):
            grid[i-1][j+1]+=1
            ticked.append((i-1,j+1))
        if j-1>=0:
            grid[i-1][j-1]+=1
            ticked.append((i-1,j-1))
    if j-1>=0:
        grid[i][j-1]+=1
        ticked.append((i,j-1))
    if j+1<len(grid[0]):
        grid[i][j+1]+=1
        ticked.append((i,j+1))
    for t in ticked:
        if grid[t[0]][t[1]]>9 and t not in flashed:
            toFlash.append(t)
    

def initialFlash(toFlash, flashed):
    #print(toFlash)
    for f in toFlash:
        if f not in flashed:
            flash(f[0],f[1], toFlash,flashed)
            flashed.append(f)
            initialFlash(toFlash,flashed)
def tick():
    flashed = []
    toFlash = []
    for row in range(len(grid)):
        for col in range(len(grid)):
            grid[row][col]+=1
            if grid[row][col]>9:
                toFlash.append((row,col))
    
    initialFlash(toFlash,flashed)
        
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            #print((row, col))
            if (row,col) in flashed:
                grid[row][col]=0           

step=0

flashcount =0

def displayGrid():
    for line in grid:
        print(*line, sep = " ", end="\n")     

#displayGrid()
#print()

while tempFlashCount!=100:
    
    tempFlashCount =0
    tick()

    print(tempFlashCount)
    step+=1
    #displayGrid()  
    #print()
print(step)
print(flashcount)