import math

invalid_list = ['2','4','5','6','8','0']

potentials = potentialCircularPrimes(1000000)

circular_list = []

for i in potentials:
	if testCircularity(i,potentials):
		circular_list.append(i)

print("The answer is" + len(circular_list))

def notCircular(n):
	if any(s in str(n) for s in invalid_list):
		return True
	else:
		return False

def potentialCircularPrimes(n):
	primes = [2,3,5]
	for i in range(6,n):
		if not notCircular(i):
			for k in range(2,math.ceil(math.sqrt(i))+1):
				if i%k == 0:
					break
				elif k == math.ceil(math.sqrt(i)):
					primes.append(i)
	return primes

def testCircularity(n, list):
	if len(str(n))==1:
		return True
	for i in range(1,len(str(n))):
		next = int(str(n)[i:]+str(n)[:i])
		if next not in list:
			break
		elif i == len(str(n))-1:
			return True
	return False
