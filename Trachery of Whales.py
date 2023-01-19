import copy
with open("directions.txt") as f:
     data = f.read()

positions = list(map(int, data.split(",")))
positions.sort()
sorted = []
weights=[]

for pos in positions:
    if pos not in sorted:
        sorted.append(pos)
for w in range(len(sorted)):
    weights.append(0)
    for pos in positions:
        if sorted[w]==pos:
            weights[w]+=1
  
weightedList = [sorted,weights]
weightedListCopy = copy.copy(weightedList)
mean = sum(sorted)/len(sorted)
priorityQueue =[]
largest=0
smallest=100
for pos in weightedList[0]:
    if pos> largest:
        largest = pos
    if pos< smallest:
        smallest= pos
print(largest)
print(smallest)
def getHeaviest(wList):
    max=0
    weight=0
    for w in range(len(wList[1])):
        #if wList[1][w] !=1:
            #print(wList[1][w])
        if wList[1][w]>weight:
            #print(str(max)+ " max "+ str(wList[1][w])+ " new max")
            max = wList[0][w]
            weight= wList[1][w]
            index = w 
            heaviest =[max, weight]
    #print(heaviest)
    priorityQueue.append(heaviest)
    return index

def fuelSum(index, wList):
    sum = 0
    for i in range(len(wList[0])):
        #print(str(index)+ " index")
        #print(str(wList[0][i])+ " position")
        #print(abs(index-wList[0][i])*wList[1][i])
        for j in range(abs(index-wList[0][i])):
            sum+= (j+1)*wList[1][i]
    return sum

# while len(priorityQueue)<15 and len(priorityQueue)<len(sorted):
#     heaviestIndex = getHeaviest(weightedList)
#     weightedList[0].pop(heaviestIndex)
#     weightedList[1].pop(heaviestIndex)
    
    #print(len(priorityQueue))
#print(weightedListCopy)
g = fuelSum(0, weightedListCopy)
gindex =0

for i in range(smallest, largest):
    s = fuelSum(i, weightedListCopy)
    #print(s)
    if s< g:
        g=s
        gindex=i
print()
print(g)
print(gindex)
#print(priorityQueue) 
print(mean)

