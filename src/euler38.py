


a = pantwo()
b = panthree()
c = panfour()
panprod= []
for i in a:
	for j in b:
		z = i * j
		if z < 10000 and len(set(str(i)+str(j)+str(z)))==9 and '0' not in set(str(i)+str(j)+str(z)):
			panprod.append(z)

panprod2 = []
for i in range(1,10):
	for j in c:
		z = i * j
		if z < 100000 and len(set(str(i)+str(j)+str(z)))==9 and '0' not in set(str(i)+str(j)+str(z)) and len(str(i))+len(str(j))+len(str(z)) == 9 :
			panprod2.append(z)



sum = 0
for i in set(panprod+panprod2):
	sum = sum + i

def pantwo():
	list = []
	for i in range(10,100):
		if str(i)[0]!=str(i)[1] and str(i)[1]!='0':
			list.append(i)
	return list

def panthree():
	list = []
	for i in range(100,1000):
		if str(i)[0]!=str(i)[1] and str(i)[1]!=str(i)[2] and str(i)[0]!=str(i)[2] and str(i)[2]!='0':
			list.append(i)
	return list

def panfour():
	list = []
	for i in range(1000,10000):
		if len(set(str(i)))==4 and '0' not in set(str(i)):
			list.append(i)
	return list

