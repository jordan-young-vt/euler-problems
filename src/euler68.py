##Slightly different implementation than 18

import re
import urllib2

def readInData():
	a = urllib2.urlopen("http://projecteuler.net/project/triangle.txt").read()
	split_number = a.split('\n')
	return split_number

def restructureData(data):
	dataStruct = []
	for i in range(len(data)):
		dataStruct.append(re.findall(r'\d+', data[i]))
	return dataStruct, dataStruct[len(dataStruct)-2]


def recurse_up(j,dataStruct,dataStruct2):
	for i in range(len(dataStruct[j])):
		dataStruct2[i] = int(dataStruct[j][i])+max(int(dataStruct2[i]),int(dataStruct2[i+1]))
	del dataStruct2[-1]

def main():
	data = readInData()
	data1, data2 = restructureData(data)
	for i in range(1,len(data2)):
		recurse_up(len(data)-2-i,data1,data2)
	return data2[0]

if __name__=="__main__":
	print(main())
