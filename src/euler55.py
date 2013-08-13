

count = 0
for i in range(10000):
	if isLychel(i):
		count=count+1


def isPalindrome(n):
	if str(n)==str(n)[::-1]:
		return True
	else:
		return False


def isLychel(n):
	num = n
	for i in range(50):
		num = num+int(str(num)[::-1])
		if isPalindrome(num):
			break
		elif i == 49:
			return True
	return False




