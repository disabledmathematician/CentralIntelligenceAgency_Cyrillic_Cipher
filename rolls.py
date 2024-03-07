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
	plt.title("Descartes Plot for Trials of Sums of Die Rolls. Charles Truscott")
	
	plt.plot([x for x in range(len(L))], L[:len(L)], color='gold', label='100 trials')
	plt.plot([x for x in range(len(L) // 2)], L[:len(L) // 2], color='silver', label='50 trials')
	plt.plot([x for x in range(len(L) // 4)], L[:len(L) // 4], color='purple', label='25 trials')
	
	x = [len(L) // 4, len(L) // 2, len(L)]
	y = [np.mean(L[:len(L) // 4]), np.mean(L[:len(L) // 2]), np.mean(L[:])]
	plt.plot(x, y, color='pink', label="running avg")
	plt.legend()
#	plt.show()
	plt.savefig('all_trials.png')
	plt.figure(1, dpi=150, figsize=[15, 7])
	plt.title("Histogram for sum of two die rolls. Charles Truscott")
	plt.hist(L, linewidth=0.5, edgecolor='black')
	plt.savefig('all_hist.png')
rolls()