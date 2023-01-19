file =  open('directions.txt', 'r')
f = file.readlines()

options = []
for line in f:
    trait = line.index("-")
    options.append((line[:trait], line[trait+1:].strip("\n")))
    if options[-1][0] !="start" and options[-1][1] != "end":
        options.append((options[-1][1], options[-1][0]))
#print(*options, sep = "\n")
#print()
lowers=[]
for o in options:
    if o[0].islower() and o[0] not in lowers:
        lowers.append(o[0])
    if o[1].islower() and o[1] not in lowers:
        lowers.append(o[1])
lowers.remove("start")
lowers.remove("end")

def search(paths, c):
    newPaths = []
    full = True
    for path in paths:
        start = path[-1]
        #print(start)
        if start !="end":
            full = False
            
            for case in options:
                count = 0
                for l in path:
                    if l == c:
                        count+=1
                #print(case, end = " case\n")

                if (case[0]==start and case[1].isupper()): # upper cases
                   # print("allo")
                    p = list(path)
                    p.append(case[1])
                   # print(p, end = " beans\n")
                    #if not in paths maybe
                    newPaths.append(p)
                    #print(newPaths)
                if case[0]==start and case[1]==c and count<2:
                    #print("ya")
                    p = list(path)
                    p.append(case[1])
                    newPaths.append(p)
                    #print(p)
                elif (case[0]==start and case[1].islower() and case[1] not in path): # lower cases
                   # print("allo")
                    p = list(path)
                    p.append(case[1])
                    newPaths.append(p)
                    #print(newPaths)
        else:
            newPaths.append(path)
                    
    if full==False:
        return search(newPaths,c)
    else:
        #print("AHHHAHAHAAHAHAHAHA")
        #print(paths)
        return paths
solutions=[]
sum = 0
print(*lowers,sep=" ")
for l in lowers:
    for case in options:
        if case[0]=="start":
            path =[]
            path.append([case[0],case[1]])
            arr = search(path,l)
            for p in arr:
                solutions.append(p)

res = []
for i in solutions:
    if i not in res:
        res.append(i)
print(len(res))
# dont go back to start, dont go back to lower case, end at end
