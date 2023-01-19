with open("directions.txt") as f:
     data = f.read()
numbers = []
index=0
switch =False
displayed = []
for c in range(len(data)):
    if data[c] == "|":
        numbers.append(data[index: c].strip("|"))
        index = c+1
    if data[c] == "\n":
        displayed.append(data[index: c].strip("\n"))
        index = c+1 
        


n=[]
d=[]
for num in numbers:
    n.append(num[:-1].split(" "))
for dis in displayed:
    d.append(dis[1:].split(" "))
displayed=d
numbers = n
#print(*displayed, sep = "\n")
#print(*numbers, sep = "\n")
uniques = []    
def initialize():
    pixels = dict()
    for i in range(1,10):
        pixels[i] = ""
    return pixels
def addCore(core, letters):
    for l in letters:
        if l not in core:
            core.extend(l)
    return core
def convert(s):
    new = ""
    remove = ""
    for x in s:
        new += x 
    return new.replace(remove,"") 

def defineLetters(nums):
    for n in nums:
        if len(n)==2:
            pixels[3] = convert(n)
            pixels[6] = convert(n)
    for n in nums:
        if len(n)==3:
            pixels[1] = convert(n).replace(pixels[3],"") 
    for n in nums:
        if len(n)==4:
            temp = convert(n).replace(pixels[3][0],"") 
            temp = temp.replace(pixels[3][1],"")
            pixels[2] = temp
            pixels[4] = temp
    poses = "abcdefg"
    rem = (pixels[1]+pixels[2]+pixels[3])
    final=""
    for l in poses:
        if l not in rem:
            final+= l
    pixels[5]= final
    pixels[7]= final

sum=0
for i in range(len(numbers)):
    
    #print(uniques)
    #print(numbers[i])
    #print(displayed[i])
    digits =""
    global pixels
    pixels = initialize()
    found = False
    defineLetters(numbers[i])
    #print(pixels)
    for case in displayed[i]:
        letters = case
        for num in numbers[i]:
            if len(num)==len(letters):
                #print("yo")
                if len(letters) == 2:
                    digits+="1"
                elif len(letters) == 3:
                    digits+="7"
                elif len(letters) == 4: 
                    digits+="4"
                elif len(letters) == 7:
                    digits+="8"
                elif len(letters) == 5 : #maybe split here
                   # print("in 5")
                    #print(pixels)
                    #print(letters)
                    #print(num)
                    if pixels[2][0] in letters and pixels[2][1] in letters:
                        digits+="5"
                    elif pixels[3][0] in letters and pixels[3][1] in letters:
                        digits+="3"
                    else:
                        digits+="2"  
                        
                elif len(letters) == 6:
                    #if pixels[2][0] in letters and pixels[2][1] in letters and pixels[5][0] in letters and pixels[5][1] in letters:
                    #print("in 6")
                    #print(pixels)
                    if pixels[3][0] in letters and pixels[3][1] in letters and pixels[5][0] in letters and pixels[5][1] in letters:
                        digits+="0"
                    elif pixels[5][0] in letters and pixels[5][1] in letters:
                        digits+="6"
                    else:
                        digits+="9"
            
                break
    print(digits)
    sum+=int(digits)
print(sum)
#178
#234569