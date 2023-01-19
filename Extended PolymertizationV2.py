import time
file =  open('directions.txt', 'r')
f = file.readlines()
initial = f[0].strip("\n")
f = f[2:]
commands = []

for line in f:
    trait = line.index(">")
    commands.append((line[:trait-1].strip(" "), line[trait+2:].strip("\n")))
doubles = []
for c in commands:
    doubles.append(c[0].strip(" "))
amounts = {x: 0 for x in doubles}
empty = dict(amounts)
let = []
for d in doubles:
    if d[0] not in let:
        let.append(d[0])
    if d[1] not in let:
        let.append(d[1])
letters = {x:0 for x in let}

def findCorresponding(c):
    for case in commands:
        if case[0]==c:
            return case[1]

for l in initial:
    letters[l]+=1
for i in range(len(initial)-1):
    sub = initial[i]+initial[i+1]
    amounts[sub]+=1

step = 0
maximum = 2000
while step < maximum:
    operations = {x: 0 for x in doubles}
    toAdd = {x:0 for x in let}
    count = 0
    for key in amounts:
        sub = key
        limit = amounts[sub]
        insert = findCorresponding(sub)    
        if amounts[sub]>0:
            letters[insert]+=limit
            operations[sub[0]+insert]+=limit
            operations[insert+sub[1]]+=limit
            operations[sub]-=limit
    for op in operations:
        amounts[op]+=operations[op] 
    print(letters)
    print(str(step)+ ": step")
    step+=1

maxL=0
minL=-1
for l in letters:
    if letters[l]>maxL:
        maxL = letters[l]
    if letters[l]< minL or minL<0:
        minL = letters[l]
dif = maxL-minL
print(dif)
