import math

reasonable_max = 150000

primeList = primes(reasonable_max)

quadraticList = []

for a in range(-101,1,2):
	b = calculateB(a)
	if b <= 1000:
		q = test_value(a,b)
		if q > 50:
			temp = []
			temp.append(a)
			temp.append(b)
			temp.append(q)
			quadraticList.append(temp)

finish(quadraticList)

def primes(n):
	primes = [2,3,5]
	for i in range(6,n):
		for k in range(len(primes)):
			if i%primes[k] == 0:
				break
			elif k == len(primes)-1:
				primes.append(i)
	return primes

def finish(list):
	maxList = []
	maxCons = 0
	for i in list:
		if i[2]>maxCons:
			maxCons = i[2]
			maxList = i
	print(maxCons)
	print(maxList)
	return maxList[0]*maxList[1]

def test_value(a,b):
	for z in range(0,100):
		if (z*z+a*z+b) not in primeList:
			return z

def calculateB(a):
	sum = 41
	for i in range(0, int((a+1)/-2)):
		sum = sum + 2*(i+1)
	return sum