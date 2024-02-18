import math
N,M,R = map(int,input().split())
mtx = [list(map(int,input().split())) for _ in range(N)]
shell = [[]*math.ceil(M/2) for _ in range(math.ceil(M/2))]
def findShell(n):
    endX,endY = N-n-1, M-n-1
    x=n
    y=n
    while True:
        if x < endX and y == n: # 아래로
            shell[n].append(mtx[x][y])
            x+=1
        elif x == endX and y < endY: # 우측으로
            shell[n].append(mtx[x][y])
            y+=1
        elif  x > n and y == endY: # 위로
            shell[n].append(mtx[x][y])
            x-=1
        elif x == n and y > n: # 좌측으로
            shell[n].append(mtx[x][y])
            y-=1
        if x == n and y== n:
            break
        if n == endX and y == endY:
            break


         
            
def moveShell(n):
    endX,endY = N-n-1, M-n-1
    x = n
    y = n
    cnt = 0
    while cnt < len(shell[n]):
        tmp = (len(shell[n]) - R + cnt) % len(shell[n])
        mtx[x][y] = shell[n][tmp]
        if x < endX and y == n: # 아래로
            x+=1
        elif x == endX and y < endY: # 우측으로          
            y+=1
        elif  x > n and y == endY: # 위로
            x-=1
        elif x == n and y > 0: # 좌측으로
            y-=1
        cnt += 1
                
            
for i in range(math.ceil(M/2)):
    findShell(i)

for i in range(math.ceil(M/2)):
    moveShell(i)
    
for xx in mtx:
    print(" ".join(map(str, xx)))