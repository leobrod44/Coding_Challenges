import time
file =  open('directions.txt', 'r')
f = file.readlines()
initial = f[0].strip("\n")
f = f[2:]
commands = []

#store commands
for line in f:
    #print(line)
    trait = line.index(">")
    commands.append((line[:trait-1].strip(" "), line[trait+2:].strip("\n")))
#print(commands)
doubles = []
for c in commands:
    doubles.append(c[0].strip(" "))
amounts = {x: 0 for x in doubles}

def findCorresponding(c):
    for case in commands:
        if case[0]==c:
            return case[1]
for i in range(len(initial)-1):
    sub = initial[i]+initial[i+1]
    amounts[sub]+=1
print(amounts)


step = 0
maximum = 3

while step < maximum:
    for key in amounts:
        sub = key
        limit = amounts[sub]
        insert = findCorresponding(sub)
        print(str(key) + " : "+str(limit))
        for i in range(limit):
            amounts[sub[0]+insert]+=1
            amounts[insert+sub[1]]+=1
            amounts[sub]-=1
    print(amounts)
    step+=1


