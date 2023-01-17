import numpy

file =  open('data.txt', 'r')
f = [x.replace('\n','') for x in file.readlines()]
text = " ".join(f)

count=0

usedChars = ''
valid =''

for c in text:
    count+=1
    
    newvalid = valid
    for i in range(len(valid)):
        if c == valid[i]:
            newvalid = valid[i+1:]
    valid= newvalid+c    
    print(valid)
    if len(valid) == 14:
        break
            
print(count)
