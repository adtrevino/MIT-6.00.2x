import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    pickAvg = []
    sameColor = 0
    
    for i in range(numTrials):
        bucket = ["r", "r", "r", "g", "g", "g"]
        pick = []
        for times in range(3):
            pick.append(random.choice(bucket))
            bucket.remove(pick[-1])
        pickAvg.append(pick)
    
    for trial in pickAvg:
        if trial.count(trial[0]) == 3:
            sameColor += 1    
    
    return sameColor/numTrials

num = 1000

print(noReplacementSimulation(num))