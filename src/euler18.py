import re
from bs4 import BeautifulSoup
import urllib2

def readInData():
	a = urllib2.urlopen("http://projecteuler.net/problem=18").read()
	soup = BeautifulSoup(a)
	numbers = soup.findAll('p')[4]
	split_number = str(numbers).split('new;">')[1].split('</p>')[0].split('<br/>\r\n')
	re.findall(r'\d+', split_number[3])
	return split_number

def restructureData(data):
	dict = {}
	for i in range(len(data)):
		dict[i]=re.findall(r'\d+', data[i])
	return dict

def recurse_up(dict,j):
	for i in range(len(dict[j])):
		dict[j][i] = int(dict[j][i])+max(int(dict[j+1][i]),int(dict[j+1][i+1]))

def main():
	split_number = readInData()
	dict = restructureData(split_number)
	for i in range(1,len(dict)):
		recurse_up(dict,len(dict)-1-i)
	return dict[0][0]

if __name__=="__main__":
	print(main())
