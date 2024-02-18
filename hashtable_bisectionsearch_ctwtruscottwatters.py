""" Linear Search as opposed to Bisection Search with Hashing and Chaining, DAT and Linked List """
""" Charles Truscott Watters

Searching for Apples in a Linear order n search takes 3 steps to find it at the 2th index
{'A': ['Air', 'Acrid', 'Apples'], 'B': ['Bait', 'Bench', 'Bananas'], 'C': ['Cill', 'Chair', 'Charles']}
Searching for Apples in a Hash Table order log2(m/n) `m keys, n slots` search takes 1 steps to find it at the 2th index
Charles Thomas Wallace Truscott Watters
Searching for Charles in a Linear order n search takes 9 steps to find it at the 8th index
{'A': ['Air', 'Acrid', 'Apples'], 'B': ['Bait', 'Bench', 'Bananas'], 'C': ['Cill', 'Chair', 'Charles']}
Searching for Charles in a Hash Table order log2(m/n) `m keys, n slots` search takes 1 steps to find it at the 2th index
Charles Thomas Wallace Truscott Watters
Searching for Bananas in a Linear order n search takes 6 steps to find it at the 5th index
{'A': ['Air', 'Acrid', 'Apples'], 'B': ['Bait', 'Bench', 'Bananas'], 'C': ['Cill', 'Chair', 'Charles']}
Searching for Bananas in a Hash Table order log2(m/n) `m keys, n slots` search takes 1 steps to find it at the 2th index
Charles Thomas Wallace Truscott Watters
613
284
483
692
480
384
706
487
388

[Program finished]

PyDroid on Samsung Galaxy Note 20 5G

Reducing algorithmic complexity

"""

def LinearSearch(L, e):
	steps = 0
	for n in range(len(L)):
		steps += 1
		if L[n] == e:
			return (L, e, steps, n)
def BisectionBucketSearch_ctwtruscottwatters(L, e):
	hashed = {}
	for x in range(len(L)):
		hashed[L[x][0]] = []
	for x in range(len(L)):
		hashed[L[x][0]].append(L[x])
	print(hashed)
	tL = hashed[e[0]]
	high = len(tL)
	low = 0
	guess = (high + low) // 2
	steps = 0
	ss = sum(ord(x) for x in e)
	while tL[guess] != e:
		if sum(ord(x) for x in tL[guess]) > ss:
			high = guess
		elif sum(ord(x) for x in tL[guess]) < ss:
			low = guess
#		elif ord(tL[guess][2]) > ord(e[2]):
#			high = guess
#		elif ord(tL[guess][2]) < ord(e[2]):
#			low = guess
		guess = (high + low) // 2
		steps += 1
	return (L, e, guess, steps)
	
for x in ["Apples", "Charles", "Bananas"]:
	L0, e0, steps0, guess0 = LinearSearch(["Air", "Acrid", "Apples", "Bait", "Bench", "Bananas", "Cill", "Chair", "Charles"], x)
	print("Searching for {} in a Linear order n search takes {} steps to find it at the {}th index".format(x, steps0, guess0))
	L1, e1, guess1, steps1 = BisectionBucketSearch_ctwtruscottwatters(["Air", "Acrid", "Apples", "Bait", "Bench", "Bananas", "Cill", "Chair", "Charles"], x)
	print("Searching for {} in a Hash Table order log2(m/n) `m keys, n slots` search takes {} steps to find it at the {}th index".format(x, steps1, guess1))
	print("Charles Thomas Wallace Truscott Watters")

for x in ["Apples", "Air", "Acrid", "Bananas", "Bench", "Bait", "Charles", "Chair", "Cill"]:
	print(sum(ord(n) for n in x))