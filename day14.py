import time
file =  open('directions.txt', 'r')
f = file.readlines()
initial = f[0].strip("\n")
f = f[2:]
commands = []
for line in f:
    print(line)
    trait = line.index(">")
    commands.append((line[:trait-1].strip(" "), line[trait+2:].strip("\n")))
print(commands)
step = 0
maximum = 40
word = initial
doubles = []
for c in commands:
    doubles.append(c[0].strip(" "))
print(doubles)
length = len(word)
while step < maximum:
    startime = time.time()
    letter = word[0]
    i=0
    while i <= len(word)-2:
        sub = ""
        sub+= word[i]+word[i+1]
        if sub in doubles:
            index = doubles.index(sub)
            # print(word, end = " current\n")
            # print(word[:(i+1)], end = " before\n")
            # print(commands[index][1], end = " new\n")
            # print(word[i+1:], end = " after\n")
            temp = word[:(i+1)] 
            # print(temp)
            word = temp+ commands[index][1] + word[i+1:] 
            # print(word, end = " current2\n")
            # print()
            i+=2
        else:
            i+=1
    length = len(word)
    print(str(len(word))+  " " + str(len(word)*2)+ " ")
    #differents = set([c for c in word])
    counts = []
    countS=0
    countN=0
    for c in word:
        count = 0
        if c=="S":
            countS+=1
        if c=="N":
            countN+=1
    print()
    print(countS)
    print(countN)
    print(len(word))
    print(countS/len(word))
    print(countN/len(word))
    print()
    print(step)
    print()
    # minC=-1
    # minL=""
    # maxC=0
    # maxL=""
    # for c in counts:
    #     if c[1]>maxC:
    #         maxC =c[1]
    #         maxL =c[0]
    #     if c[1]<minC or minC<0:
    #         minC =c[1]
    #         minL =c[0]
    endtime = time.time()
    print(endtime-startime)
    step+=1


