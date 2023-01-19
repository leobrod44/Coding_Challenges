file =  open('directions.txt', 'r')
f = file.readlines()
position = [0,0,0]

lines = []
for line in f:
    lines.append(line.strip())
mostbit = ""
leastbit = ""
zeroPos = []
newBit = []
onePos = []

count = 0
#lines = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
length = len(lines[0])
oxygen = lines
Co2 = lines
for i in range(length):
    onePos = []
    zeroPos = []
    count = 0
    if len(oxygen)>1:
        for l in oxygen:
            if int(l[i])==0:
                zeroPos.append(l)
            if int(l[i])==1:
                onePos.append(l)
        
        if len(zeroPos)>len(onePos):
            oxygen = zeroPos
        elif len(zeroPos)<=len(onePos):
            oxygen= onePos
    print("oxygen")
    print(oxygen)
    onePos = [] 
    zeroPos = []
    if len(Co2)>1:
        for l in Co2:
            if int(l[i])==0:
                zeroPos.append(l)
            if int(l[i])==1:
                onePos.append(l)
        if len(zeroPos)>len(onePos):
            Co2 = onePos
        elif len(zeroPos)<=len(onePos):
            Co2= zeroPos
    count+=1
    print("Co2")
    print(Co2)
print(oxygen)
print(Co2)
gamma = int(oxygen[0],2)
epsilon=int(Co2[0],2)
print(gamma)
print(epsilon)
print(gamma*epsilon)
