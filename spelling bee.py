file =  open('directions.txt', 'r')
f = file.readlines()
words = []
for line in f:
    words.append(line.strip("\n"))
toFind =["k", "n", "i", "c","n"]

confirmed = []
# for word in words:
#     for c in word:
#         if c not in toFind:
#             words.remove(word)

for word in words:
    count = 0
    for l in toFind:
        if l in word:
            count+=1
    if count == len(toFind):
        confirmed.append(word)
print(*confirmed, sep = "\n")
