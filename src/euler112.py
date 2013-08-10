import time
def main():
    t1 = time.time()
    print(findMinBouncy(0.99))
    t2 = time.time()
    print('Total Run Time in Seconds: '+str(t2-t1))

def isBouncy(n):
    if len(str(n))==1:
        return False
    if not (isIncreasing(n) or isDecreasing(n)):
        return True
    return False

def isIncreasing(n):
    for i in range(len(str(n))-1):
        if str(n)[i]>str(n)[i+1]:
            break
        elif i == len(str(n))-2:
            return True
    return False

def isDecreasing(n):
    for i in range(len(str(n))-1):
        if str(n)[i]<str(n)[i+1]:
            break
        elif i == len(str(n))-2:
            return True
    return False

def findMinBouncy(n):
    count = 0
    countBouncy = 0
    ratio = 0
    i = 1
    while ratio<n:
        if isBouncy(i):
            countBouncy=countBouncy+1
        count = count+1
        ratio = float(countBouncy)/float(count)
        i = i+1
    return count

if __name__ == "__main__":
    main()

