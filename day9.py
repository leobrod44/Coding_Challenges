file =  open('directions.txt', 'r')
f = file.readlines()
global points
points=[]
for line in f:
    points.append(line.strip("\n"))
print(points)
lowPoints = []
basins = []

def horizontalCheck(i,j):
    if j>=0 and j<len(points[i])-1 and int(points[i][j])!=9 :
        alreadyThere = False
        for row in basinCoords:
             if (i,j) in row:
                 alreadyThere = True
        if alreadyThere==False:
            horizontal.append((i, j)) 
        print("ya")
        return True
        
    else:
        print("na")
        return False

                
def horizontalBasin(i,j):
    left = 1
    right = 1
    leftLimit = False
    rightLimit = False
    global horizontal
    horizontal = [(i,j)]
    while rightLimit == False and leftLimit == False:
        print(horizontal)
        leftLimit = horizontalCheck(i, j-left)
        left+=1
        rightLimit = horizontalCheck(i, j+right)
        right+=1
    return horizontal

def findBasin(i,j):
    global basinCoords
    basinCoords =[]
    lastCoords = []
    basinCoords.append(horizontalBasin(i,j))
    while basinCoords != lastCoords:
        lastCoords = basinCoords
        for row in basinCoords:
            for coord in row:
                basinCoords.append(horizontalBasin(coord[0],coord[1]+1))
        print(lastCoords)
        print(basinCoords)
    

    return len(basinCoords)

def searchBot(i,j):
   
    if j+1<len(points[i]) and (i,j+1) not in coords and int(points[i][j+1]) != 9:
        coords.append((i,j+1))
        print(coords)
        searchBot(i,j+1)
    if j-1>=0 and (i,j-1) not in coords and int(points[i][j-1]) != 9:
        coords.append((i,j-1))
        print(coords)
        searchBot(i,j-1)
    if i+1<len(points) and (i+1,j) not in coords and int(points[i+1][j]) != 9:
        coords.append((i+1,j))
        print(coords)
        searchBot(i+1,j)
    if i-1>=0 and (i-1,j) not in coords and int(points[i-1][j]) != 9:
        coords.append((i-1,j))
        print(coords)
        searchBot(i-1,j)
    

for i in range(len(points)):
    for j in range(len(points[0])):
        point = int(points[i][j])
        left = int(points[i][j-1]) if j>0 else 9
        right = int(points[i][j+1]) if j< len(points[i])-1 else 9
        top = int(points[i-1][j]) if i>0 else 9
        bottom = int(points[i+1][j]) if i< len(points)-1 else 9
        if point< left and point < right and point< top and point< bottom:
            lowPoints.append(point)
            global coords
            coords = []
            searchBot(i,j)
            print(coords)
            basins.append(len(coords))
print(basins)
max1=0
max2=0
max3=0
for b in basins:
    if b>=max1:
        max1 =b
basins.remove(max1)
for b in basins:
    if b>=max2:
        max2 =b
basins.remove(max2)
for b in basins:
    if b>=max3:
        max3 =b

risk = max1*max2*max3
print(risk)