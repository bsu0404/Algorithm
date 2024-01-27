import sys
N, R, C = map(int,input().split())
array =[[1]*N for _ in range(N)]
answer =0

def findSquare(x,y,n):
    count = int(n/2)
    global answer    
    AREA = [[x,y],[x,y+count],[x+count,y],[x+count,y+count]]
    
    
    for xx,yy in AREA:
        if count ==1:
            if xx==R and yy ==C:
                print(answer)
                sys.exit()
            answer+=1
        else:
            if(xx+count<R or yy+count<C):
                answer+=count**2
            else:
                findSquare(xx,yy,count)

findSquare(0,0,2**N)