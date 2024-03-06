import random
import matplotlib.pyplot as plt
import numpy as np
def rolls():
	d1 = [x for x in range(1, 7)]
	d2 = [x for x in range(1, 7)]
	L = []
	for x in range(100):
		L.append(random.choice(d1) + random.choice(d2))
	plt.figure(0, dpi=150, figsize=[15, 7])
	plt.title("Charles Truscott")
	plt.plot([x for x in range(len(L) // 4)], L[:len(L) // 4], color='purple', label='25 trials')
	plt.plot([x for x in range(len(L) // 2)], L[:len(L) // 2], color='silver', label='50 trials')
	plt.plot([x for x in range(len(L))], L[:len(L)], color='gold', label='100 trials')
	x = [len(L) // 4, len(L) // 2, len(L)]
	y = [np.mean(L[:len(L) // 4]), np.mean(L[:len(L) // 2]), np.mean(L[:])]
	plt.plot(x, y, color='pink', label="running avg")
	plt.legend()
	plt.savefig('100_trials.png')
rolls()