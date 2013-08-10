import time
def main():
    ts1 = time.time()
    a=all_perms('0123456789')
    list=[]
    for x in a:
        if hasProperty(x):
            list.append(int(x))

    print(sum(list))
    ts2 = time.time()
    print('Runtime in Seconds: ' + str(ts2-ts1))
    

def hasProperty(n):
    if int(n[1:4])%2==0 and int(n[2:5])%3==0 and int(n[3:6])%5==0 and int(n[4:7])%7==0 and int(n[5:8])%11==0 and int(n[6:9])%13==0 and int(n[7:10])%17==0:
        return True
    else:
        return False
    
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

if __name__ == "__main__":
    main()
