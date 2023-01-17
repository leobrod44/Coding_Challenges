import numpy

file =  open('data.txt', 'r')
f = [x.replace('\n','') for x in file.readlines()]
plays = []
for play in f:
    play = play.replace('A','0')
    play = play.replace('X','0')
    play = play.replace('B','1')
    play = play.replace('Y','1')
    play = play.replace('C','2')
    play = play.replace('Z','2')
    play = play.replace(' ', '')
    plays.append(play)


score = 0
for play in plays:
    print(play)
    opp = int(play[0])
    outcome = int(play[1])
    if outcome == 1:
        score+=(opp+3+1)
    elif outcome == 2:
        for i in range(opp,opp+3):
            elem = i%3
            if elem !=opp:
                score+=(elem+6+1)
                break
    else:
        for i in range(opp,opp-3,-1):
            elem = i%3
            if elem !=opp:
                score+=(elem+1)
                break          

print(score)

    



