# Needed Score Combination


scores = [93, 96, 95, 89, 94]                                        # set current scores
average = 95                                                         # set desired average
neededscore = (average*(len(scores) +2)) - (sum(scores))             # formula for calculating needed score


# seeing what numbers add up to neededscore


from itertools import permutations                                                               

numbers = range(100)
target_number = average

solutions = [pair for pair in permutations(numbers, 2) if sum(pair) == 95]

print('Solutions:', solutions)