
alphabetDict = {
	'A':1,'B':2, 'C':3, 'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26
}

tri = triangleNumberGenerator(100)

file = '/Users/jyoung/Desktop/hql_scripts/words.txt'

with open(file) as f:
	data = f.readlines()

dataList = data[0].replace('"','').split(',')

count=0
for i in dataList:
	if countWord(i) in tri:
		count=count+1

print(count)

def countWord(word):
	sum = 0
	for i in word:
		sum = sum + alphabetDict[i]
	return sum

def triangleNumberGenerator(z):
	list = []
	for i in range(1,z+1):
		list.append(int(0.5*i*(i+1)))
	return list




	