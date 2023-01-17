import math
print("starting")
file =  open('directions.txt', 'r')
f = file.readlines()
fishesChar= f[0].split(',')
global fishes
fishes=[]
# with open("day6.txt") as f:
#     data = f.read()

#print(list(map(int, fishes.split(","))))
for i in range(len(fishesChar)):
    fishes.append(int(fishesChar[i]))

def tick():
    global fishes
    length = len(fishes)
    for i in range(length):
        if fishes[i]==0:
            fishes[i]=6
            createFish()
        else:
            fishes[i]-=1

def createFish():
    global fishes
    fishes.append(8)
    #print(fishes)

day=0
dayLimit=80


iP = 5
rate1 = 1/7
rate2 = 1/8
delay = 0
eP = iP * math.pow(2, math.floor(rate1*((dayLimit+delay))))
#eP = iP * math.floor((math.pow(2, (rate1*((dayLimit+delay))))+ (math.pow(2,(rate2*(dayLimit+delay)))))/2)
#print(math.pow(2, math.floor(rate1*((dayLimit+delay)))))
#print(math.floor(rate2*dayLimit))
print(eP)
#print(day)
while(day<dayLimit):
    print(day, end= ' ')
    # #print(fishes, end = " ")
    print(len(fishes), end = ' ')
    print(len(fishes)/5, end = "\t")
    print()
    tick()
    day+=1

print(len(fishes))