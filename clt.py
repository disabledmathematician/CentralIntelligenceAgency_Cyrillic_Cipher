import random
import numpy as np
import matplotlib.pyplot as plt
def Plots():
	means = []
	c = 0
	for n in [50, 100, 500, 1000]:
		for x in range(n):
			x = np.mean(np.random.randint(-25, 25, n))
			means.append(x)
		plt.figure(c, dpi=120, figsize=[7, 7])
		plt.hist(means, bins=10, histtype='bar', ec='black')
		plt.savefig('clts-{}.png'.format(c))
		c += 1
# Central Limit Theorem
# Charles
Plots()
		