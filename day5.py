import numpy as np

print("starting")
file =  open('directions.txt', 'r')
f = file.readlines()
coordinates = []
#split file into coordinates
for l in f:
    l = l[:-1].split(" -> ")
    first = l[0].split(",")
    second = l[1].split(",")
    line = []
    first[0] = int(first[0])
    first[1] = int(first[1])
    second[0] = int(second[0])
    second[1] = int(second[1])
    line.append(first)
    line.append(second)
    coordinates.append(line)

# horizontal and vertical points
def getFlats(coords):
    flats = []
    for pair in coords:
        if pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]:
            flats.append(pair)
    return flats

flatCoords = getFlats(coordinates)
coords = []
duplicates = []
horizontal = True
for coord in coordinates:
    xRange = coord[1][0]-coord[0][0]
    yRange = coord[1][1]-coord[0][1]
    smallX = coord[0][0] if xRange>=0 else coord[1][0]
    smallY = coord[0][1] if yRange>=0 else coord[1][1]
    if xRange==0 or yRange==0:
        for i in range(smallX, smallX+abs(xRange)+1):
            for j in range(smallY, smallY+abs(yRange)+1):
                if [i,j] in coords and [i,j] not in duplicates:
                    duplicates.append([i,j])
                coords.append([i,j])
    else:
        start = coord[0]
        yStep= 0
        xSign = 1 if xRange>0 else -1
        ySign = 1 if yRange>0 else -1
        j = start[1]
        for i in range(start[0], start[0]+xRange+xSign,xSign):
            if [i,j] in coords and[i,j] not in duplicates:
                duplicates.append([i,j])
            coords.append([i,j])
            j += ySign 

print(len(duplicates))