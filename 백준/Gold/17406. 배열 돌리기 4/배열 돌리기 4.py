import math
import copy
N,M,K = map(int,input().split())
mtx = [list(map(int,input().split())) for _ in range(N)]
originalMtx = copy.deepcopy(mtx)
direct = [list(map(int,input().split())) for _ in range(K)]
shell = [[]*math.ceil(M/2) for _ in range(math.ceil(M/2))]

R = 1 # 1개씩 이동
order = []
def dfs(arr):
    global order
    if len(arr) == K:
        order.append(arr.copy())
        return
    for i in range(0,K):
        if i in arr:
            continue
        arr.append(i)
        dfs(arr)
        arr.pop()

dfs([])

def findShell(n,centerX,centerY,w):
    endX,endY = centerX-1+w,centerY-1+w
    startX,startY=centerX-1-w,centerY-1-w
    x,y = startX,startY

    while True:
        if x == startX and y < endY: # 우측으로
            shell[n].append(mtx[x][y])
            y+=1
        elif x < endX and y == endY: # 아래로
            shell[n].append(mtx[x][y])
            x+=1
        elif x == endX and y > startY: # 좌측으로
            shell[n].append(mtx[x][y])
            y-=1
        elif  x > startX and y == startY: # 위로
            shell[n].append(mtx[x][y])
            x-=1

        if x == startX and y== startY:
            break

            
def moveShell(n,centerX,centerY,w):
    endX,endY = centerX-1+w,centerY-1+w
    startX,startY=centerX-1-w,centerY-1-w
    x,y = startX,startY

    cnt = 0
    while cnt < len(shell[n]):
        tmp = (len(shell[n]) - R + cnt) % len(shell[n])
        mtx[x][y] = shell[n][tmp]
        if x == startX and y < endY: # 우측으로          
            y+=1
        elif x < endX and y == endY: # 아래로
            x+=1
        elif x == endX and y > startY: # 좌측으로
            y-=1 
        elif  x > startX and y == startY: # 위로
            x-=1

        cnt += 1

minSum = float("inf")

for p in order: #p : 순서배열 
    mtx = copy.deepcopy(originalMtx)
    for q in p: # q: 순서
        direction = direct[q]
        centerX, centerY, w = direction
        shell = [[]*math.ceil(w) for _ in range(w)]

        for i in range(w):
            findShell(i,centerX, centerY, w-i)

        for i in range(w):
            moveShell(i,centerX, centerY, w-i)

    minSum = min(minSum,min(map(sum,mtx)))

print(minSum)