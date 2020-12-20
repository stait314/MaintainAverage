# Needed Score Combination


scores = [93, 96, 95, 89, 94]                                        # set current scores
average = 95                                                         # set desired average
C = (average*(len(scores) +2)) - (sum(scores))                       # formula for calculating needed score                                                             


# seeing what numbers add up to neededscore


from itertools import permutations                                                               

numbers = range(200)
target_number = C
solutions = [pair for pair in permutations(numbers, 2) if sum(pair) == C]

 
result = [i for i in solutions if i[1] <= 100]                        # remove variables that are over 100


print ("Resultant tuple list: ", str(result))                           



