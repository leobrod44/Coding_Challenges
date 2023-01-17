file =  open('directions.txt', 'r')
f = file.readlines()
position = [0,0,0]
lines = []
distances = []

for line in f:
    lines.append(line.strip())

for l in lines:
    distances.append(l[-1])
    command = ""
    distance = l[-1]
    if l[:-1]=="forward ":
        position[0]+=int(distance)
        mult = position[2]*int(distance)
        position[1]+=mult
    if l[:-1]=="up ":
        #position[1]+=int(distance)
        position[2]-=int(distance)
    if l[:-1]=="down ":
        #position[1]-=int(distance)
        position[2]+=int(distance)
    print(position)
result = position[0]*position[1]
print(result)

