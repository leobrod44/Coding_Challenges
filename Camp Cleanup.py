import numpy

file =  open('data.txt', 'r')
f = [x.replace('\n','') for x in file.readlines()]
sections = [[y.split('-') for y in x.split(',')] for x in f]
print(sections)
count = 0
for case in sections:
    row1 = case[0]
    row2 = case[1]
    if int(row1[0])>= int(row2[0]) and int(row1[0])<= int(row2[1]):
        count+=1
    elif int(row1[1])>= int(row2[0]) and int(row1[1])<= int(row2[1]):
        count+=1
    elif int(row2[0])>= int(row1[0]) and int(row2[0])<= int(row1[1]):
        count+=1
    elif int(row2[1])>= int(row1[0]) and int(row2[1])<= int(row1[1]):
        count+=1

print(count)
