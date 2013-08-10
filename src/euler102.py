def main():
        file = "triangles.txt"

        with open(file) as f:
                data = f.readlines()

        cnt = 0
        for i in range(len(data)):
                tmp = data[i].replace("\n","").split(",")
                if containsOrigin(int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3]),int(tmp[4]),int(tmp[5])):
                        cnt = cnt + 1
        print(cnt)


def containsOrigin(x1,y1,x2,y2,x3,y3):
	x1x2 = crossesYAxis(x1,x2)
	x2x3 = crossesYAxis(x2,x3)
	x1x3 = crossesYAxis(x1,x3)
	if (x1x2 and x2x3 and crossPoint(x1,y1,x2,y2)+crossPoint(x2,y2,x3,y3)==0) or (x1x2 and x1x3 and crossPoint(x1,y1,x2,y2)+crossPoint(x1,y1,x3,y3)==0 )or (x2x3 and x1x3 and crossPoint(x2,y2,x3,y3)+crossPoint(x1,y1,x3,y3)==0):
		return True
	else:
		return False
		
def crossesYAxis(x1, x2):
	if (x1 < 0 and x2 > 0) or (x1 > 0 and x2 < 0):
		return True
	else:
		return False

def crossPoint(x1,y1,x2,y2):
	slope = float((y2-y1))/float((x2-x1))
	yIntercept = y1+(0-x1)*slope
	if yIntercept >= 0:
		return 1
	else:
		return -1

if __name__ == "__main__":
        main()
