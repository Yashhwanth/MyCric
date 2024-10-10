overs=int(input("no of overs to be played"))
balls=overs
over_count=0
tballs=balls
batsmans={}
batsmanMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
bowlers={}
bowlsmap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wb":0,"nb":1,"db":0,"wk":0,"by":0,"lb":0}
score={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"wb":1,"nb":1,"db":0,"wk":0,"by":0,"lb":0,"stm":0}
scoreFreq={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wb":0,"nb":0,"db":0,"wk":0,"by":0,"lb":0,"rtd":0}
wicketsMap={"b":"bowled","c":"caught","lbw":"lbw","c&b":"caught&bowled","ro":"runout","stm":"stumped","hw":"hitwicket","hb":"handled the ball","obs":"obstructing the feild","to":"timedout","rtdo":"retired out"}
wicketFreq={"b":0,"c":0,"lbw":0,"c&b":0,"ro":0,"stm":0,"hw":0,"hb":0,"obs":0,"to":0,"rtdo":0}
scoreMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wk":0,"wb":0,"nb":0,"by":0,"lb":0,"rtd":0}
batsmanMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
total=0
wickets=0
extras=0
playing_batsman={"bat1":0,"bat2":0}
s="bat1"
ns="bat2"
def strikeRotate(s,ns,runs):
    if int(runs)%2!=0:
        s,ns=ns,s
        return s,ns
    return ns,s
def inputScenario(a): # function to get the scenario present in corr. maps
    while a not in score:
        a = input("re enter")
    return a
def wicketornot(x,b):
    if (x=="wb") and (b=="stm" or b=="ro" or b=="obs" or b=="hw"): #in wide, these 4 cases are only out
        return True
    if (x=="nb") and (b=="ro" or b=="obs" or b=="hw"): # in nb these 3 cases are out
        return True
    if x=="fh" and (b=="ro" or b=="obs" or b=="hw"): # in fh these 3cases are out
        return True
    return False
while balls: #if there is a ball it has too be bowled

    curr_playing_batsman=playing_batsman
    c=(tballs-balls)%6+1 # just to ask input score for each ball
    inputscene=input("enter score of {} ball".format(c)) #scenaio when ball is bowled
    x=inputScenario(inputscene) # to get correct scenario
    if x=="wb" or x=="nb" or x=="by" or x=="lb": #runs can be scored even in illegal balls
        extra_in_illegal_ball=input("enter extra scenario") #what happened in illegal ball
        if extra_in_illegal_ball=="wk": #if wicket in illegal delivery,only in some cases its out
            wicketruns=input("runs before wicket") #may score runs before getting out
            wickettype=input("type of wicket") # get wicket type
            if wicketornot(x,wickettype): #function to check whether its an out in illegaal ball or not
                wickets+=1 #if its out then increase wickets
                total += score[x]+score[wicketruns] #update score
                striker=strikeRotate(s,ns,wicketruns)
                curr_playing_batsman[s]+=score[wicketruns]
                print(curr_playing_batsman)
                scoreFreq[x] += 1 #update score freq
                scoreFreq[wicketruns] += 1 #update score freq
                scoreMap[x] += score[x]+score[wicketruns] #update score map
                wicketFreq[wickettype]+=1 #update wicket freq
        else: #if its not out in illegal ball,still score can be scored
            extra_runs=inputScenario(extra_in_illegal_ball) #extra runs in illegal ball
            scoreFreq[x]+=1 #update score freq
            scoreFreq[extra_runs]+=1 #update score freq
            total+=score[extra_runs]+score[x] #update total
            scoreMap[x]+=score[x]+score[extra_runs] #update score map
        if (x=="by" or x=="lb"):
            balls-=1
        print("balls",balls)
    elif x=="wk":
        typeofw=input("type of dis")
        total += score[x]
        scoreFreq[x] += 1
        scoreMap[x]+=score[x]
        wicketFreq[typeofw] += 1
        balls-=1
    elif x=="db":
        pass
    else:      # from 1-6
        batsmanMap[x]+=1
        curr_playing_batsman[s]+=score[x]
        s,ns=strikeRotate(s,ns,x)
        print(curr_playing_batsman)
        print(s,ns)
        total+=score[x]
        scoreFreq[x] += 1
        scoreMap[x]+=score[x]
        balls -= 1
    if c == 6:  # if c is 0, it means the over is complete
        s,ns=strikeRotate(s,ns,0)
        print(s,ns)
        print(curr_playing_batsman)
        over_count += 1  # increment the over count
        '''print(f"End of over {over_count}:")
        print(f"Total Score: {total}, Wickets: {wickets}, Extras: {extras}")
        print(f"Score Frequency: {scoreFreq}")
        print(f"Wicket Frequency: {wicketFreq}")
        print(f"Balls Remaining: {balls}")'''



'''print(total)
        print(scoreMap)
        print(scoreFreq)
        print(wicketFreq)
        print("balls",balls)'''

