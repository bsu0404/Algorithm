N = int(input())
array = [list(map(int,input().split())) for _ in range(N)]

blue=0
white=0

def checkFull(x, y, count):
    tmp = array[x][y]
    for i in range(x, x + count):
        for j in range(y, y + count):
            if array[i][j] != tmp:
                return False
    return True

def addAns(num):
    global white, blue
    if num==0:
        white+=1
    if num==1:
        blue+=1

def findSquare(x,y,n):
    global blue , white 
    count = int(n/2)   
    AREA = [[x,y],[x+count,y],[x,y+count],[x+count,y+count]]
    
    for xx,yy in AREA:
        color =  array[xx][yy] 
        if checkFull(xx,yy,count):
            addAns(color)
        else:
            if count ==1:
                addAns(color)
                return
            findSquare(xx,yy,int(n/2))

if not checkFull(0,0,N):
    findSquare(0,0,N)
else:
    addAns(array[0][0])
    
print(white)
print(blue)
