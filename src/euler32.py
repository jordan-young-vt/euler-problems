
list = []
for i in range(9182,10000):
	x = set(str(i)+str(i*2))
	if len(x)==9 and '0' not in x:
		list.append(i)

print(str(max(list))+str(max(list)*2))

def findMax(list):
	max = 0

	for i in list:
