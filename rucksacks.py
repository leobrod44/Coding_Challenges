import numpy

file =  open('data.txt', 'r')
f = [x.replace('\n','') for x in file.readlines()]
groups = [[]]
count = 0

for line in f:
    if count == 3:
        count = 0
        groups.append([])
    groups[-1].append(line)
    count+=1
    
tot = 0
for g in groups:
    sames = []
    first = g[0]
    for c in first:
        if c in g[1] and c in g[2]:
            if c.isupper():
                tot+= (ord(c)-38)
            else:
                tot+= (ord(c)-96)
            break
print(tot)