file =  open('directions.txt', 'r')
f = file.readlines()

numsStr = str(f[0])
nums=[]
index = -1
for n in range(len(numsStr)):
    if numsStr[n] == ",":
        nums.append(int(numsStr[index+1:n]))
        index = n
print(nums)
grid = []
numbers = []
f.remove(f[0])
count = 0
for line in f:
    line = line.replace("  ", " ")
    marker = -1
    currentLine = []
    for i in range(1,len(line)):
        if line[i]==" " or i==len(line)-1: 
            currentLine.append(int(line[marker+1:i])) 
            marker = i
    if currentLine:
        grid.append(currentLine)
        
    if count==5:
        numbers.append(grid)
        grid = []
        count = -1
    count+=1

foundNumber =0
found = False
sheetNum = 0
lastSheet = []
for num in nums:
    for sheet in numbers:
        found = False
        s = numbers.index(sheet)
        for line in sheet:
            #print(line)
            if int(num) in line:
                print(str(num)+ " cur num")
                print(s)
                print(len(numbers))
                n =line.index(int(num))
                print(numbers[s])
                line[n]=-1
                for i in range(5):
                    rowCount=0
                    colCount=0
                    for j in range(5):
                        if numbers[s][i][j]==-1:
                            rowCount+=1
                        if numbers[s][j][i]==-1:
                            colCount+=1
                        if rowCount == 5 or colCount == 5:
                            foundNumber = int(num)
                           
                            lastSheet = numbers.pop(s)
                            found = True
                            break
                    if found == True:
                        break
                if found == True:
                    break
            if found == True:
                break
sum=0
print(*lastSheet, sep = "\n")
print("beans")
print(numbers)
for i in range(5):
    for j in range(5):
        if lastSheet[i][j]!=-1:
            sum+= lastSheet[i][j]
                    
print(foundNumber)
print(sum*foundNumber)
