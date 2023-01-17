
file =  open('directions.txt', 'r')
f = file.readlines()
opps = ["]",")","}",">"]
def opp(char):
    if char=="[":
        return "]"
    if char=="(":
        return ")"
    if char=="{":
        return "}"
    if char=="<":
        return ">"
    if char=="]":
        return "["
    if char==")":
        return "("
    if char=="}":
        return "{"
    if char==">":
        return "<"
    
errorList = []
incomplete =[]
for line in f:
    encountered = []
    expected = []
    errors = []
    for char in line:
        if char in opps:
            if char == expected[-1]:
                expected.pop(len(expected)-1)
            else:
                errors.append(char)
                break
        else:
            encountered.append(char)
            expected.append(opp(char))
        if char == "\n":
            incomplete.append(line.strip("\n"))

missing = []
def findMissing(line):
    found = False
    for i in range(len(line)-1):
        if line[i+1] == opp(line[i]):
            line.pop(i+1)
            line.pop(i)
            findMissing(line)
            break
    missing = []
    for i in range(len(line)-1, -1,-1):
        missing.append(opp(line[i]))
    return missing

for line in incomplete:
    current = [c for c in line]
    missing.append(findMissing(current))

print(*missing, sep ="\n")
scores = []
for line in missing:
    score = 0
    for c in line:
        score*=5
        if c=="]":
           score+=2
        if c==")":
           score+=1
        if c=="}":
           score+=3
        if c==">":
           score+=4
    scores.append(score)
scores.sort()
middle = int(len(scores)/2)
print(scores)
print(scores[middle])

