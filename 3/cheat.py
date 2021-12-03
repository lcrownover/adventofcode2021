from collections import Counter

ll = [x for x in open('inputs.txt').read().strip().split('\n')]

theta = ''
epsilon = ''
for i in range(len(ll[0])):
	common = Counter([x[i] for x in ll])

	if common['0'] > common['1']:
		ll = [x for x in ll if x[i] == '0']
	else:
		ll = [x for x in ll if x[i] == '1']
	theta = ll[0]

ll = [x for x in open('inputs.txt').read().strip().split('\n')]
for i in range(len(ll[0])):
	common = Counter([x[i] for x in ll])

	if common['0'] > common['1']:
		ll = [x for x in ll if x[i] == '1']
	else:
		ll = [x for x in ll if x[i] == '0']
	if ll:
		epsilon = ll[0]
print(int(theta,2)*int(epsilon,2))
