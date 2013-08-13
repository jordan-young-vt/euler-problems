def triangleNumberGenerator(z):
	list = []
	for i in range(1,z+1):
		list.append(int(0.5*i*(i+1)))
	return list

def pentNumberGenerator(z):
	list = []
	for i in range(1,z+1):
		list.append(int(0.5*i*(3*i-1)))
	return list

def hexNumberGenerator(z):
	list = []
	for i in range(1,z+1):
		list.append(int(i*(2*i-1)))
	return list

def main(max):
	t = triangleNumberGenerator(max)
	p = pentNumberGenerator(max)
	h = hexNumberGenerator(max)

	threeList = [] 

	for x in h:
		if x in t and x in p:
			threeList.append(x)
	return threeList
