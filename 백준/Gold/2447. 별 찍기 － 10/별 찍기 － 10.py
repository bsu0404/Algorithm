
N = int(input())
array = [[' ' for _ in range(N)] for _ in range(N)]

def drawBox(x,y,n):
    count = int(n/3)   
    AREA = [[x,y],[x,y+count],[x,y+count*2],
            [x+count,y],[x+count,y+count*2],
            [x+count*2,y],[x+count*2,y+count],[x+count*2,y+count*2]]
    
    for xx,yy in AREA:
        if count == 1:
            array[xx][yy] = '*'
        else:       
            drawBox(xx,yy,int(n/3))

drawBox(0,0,N)

for s in array :
    print("".join(s))