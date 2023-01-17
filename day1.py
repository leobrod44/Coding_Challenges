import time
file =  open('radar.txt', 'r')
increase = 0
pastLine = 199
f = file.readlines()
lines = []
sum =0
sums = []
past = 199
for line in f:
    lines.append(line)

for i in range(len(lines)-2):
    sum = int(lines[i])+int(lines[i+1])+int(lines[i+2])
    sums.append(sum)
    print(sum)
past = sums[0]
for s in sums:
    if s> past:
        increase+=1

        print(str(s)+" greater "+ str(past))
    past = s
print(increase)