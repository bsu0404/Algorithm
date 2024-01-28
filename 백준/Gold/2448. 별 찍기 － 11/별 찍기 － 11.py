
N = int(input())
array = [[' ' for _ in range(2*N)] for _ in range(N)]

def drawStar(x,y):
    AREA = [[0,0],[1,-1],[1,1],[2,-2],[2,-1],[2,0],[2,1],[2,2]]
    for xx,yy in AREA:
        array[xx+x][yy+y]='*'

def drawTriangle(x,y,n): #[x,y] , 세로 높이
    if n==3:
        drawStar(x,y)
        return

    AREA = [[x,y],[x+int(n/2),y-int(n/2)],[x+int(n/2),y+int(n/2)]]
    
    for xx,yy in AREA:       
        drawTriangle(xx,yy,int(n/2))

drawTriangle(0,N-1,N)

for s in array :
    print("".join(s))