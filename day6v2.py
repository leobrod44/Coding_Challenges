import math
print("starting")
file =  open('directions.txt', 'r')
f = file.readlines()
fishesChar= f[0].split(',')
global fishes
fishes=[]
initialFishes =[]
for i in range(len(fishesChar)):
    fishes.append((int(fishesChar[i])))

breed = dict()
for i in range(0, 10):
    breed[i] = 0
for i in fishes:
    breed[i] += 1

print(breed)
x = 0

while x < 256:
    for fi in range(0, 10):
        if fi == 0:
            breed[9] += breed[fi]
            breed[7] += breed[fi]
            breed[fi] = 0
        else:
            breed[fi - 1] += breed[fi]
            breed[fi] = 0
    print(breed)
    x += 1

print(sum(breed.values()))