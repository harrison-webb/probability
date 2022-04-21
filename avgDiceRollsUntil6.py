import random
import matplotlib.pyplot as plt
from tqdm.auto import tqdm

N = 50000
totalRolls = 0
idx = []
rollsByTrial = []
avgRolls = []

for i in tqdm(range(N)): #repeat experiment N times
	numRolls = 0
	diceRoll = 0
	
	while diceRoll != 6: #roll until 6 is rolled
		diceRoll = random.randint(1,6)
		numRolls += 1
		totalRolls += 1

	idx.append(i + 1)
	rollsByTrial.append(numRolls)
	avgRolls.append(totalRolls / (i+1))


plt.plot(avgRolls)
plt.show()
