'''
4 people are playing a game where each has an equal probability of winning [P(player x wins game) = .25]. The game is repeated 6 times. What is the probability that at least 1 person wins no games?

Equivalent to:
Roll a 4 sided dice 6 times. What is the probability that at least 1 number is not rolled?

'''
from secrets import randbelow
import matplotlib.pyplot as plt


successes = 0 #success defined as at least 1 item not occuring in the 6 repetitions
successList = []
probabilities = []

numTrials = 500000
X = range(numTrials)
#Experiment loop
for i in X:

	winners = []
	
	#Play 'game' 6 times/roll dice 6 times
	for j in range(6):
		winners.append(randbelow(4) + 1)

	if (1 not in winners or 
			2 not in winners or 
			3 not in winners or 
			4 not in winners):
		successes += 1

	probabilities.append(successes / (i+1))
	#print("# Successes so far: ", successes)
	#print(f"P(success) = {successes/(i+1)} \n")

print(f"Final probability after {numTrials} trials: {successes/numTrials}")

plt.plot(X, probabilities)
plt.show()
	