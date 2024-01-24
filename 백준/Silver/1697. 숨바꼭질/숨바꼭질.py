from collections import deque

N,K= map(int,input().split())

def bfs():
    minCount = float("inf")
    needVisit = deque()
    x = N
    visited = [0] *100001 
    needVisit.append([x,0])
    visited[x] = 1
    
    while len(needVisit)>0:
        x, count = needVisit.popleft()

        MOVE = [-1,1,x] 
        if x == K :
            minCount = min(count, minCount)

        for move in MOVE:
            nx = x +  move           
            if (0 <= nx <= 100000)  and (visited[nx] == 0) :
                visited[nx] = 1
                needVisit.append([nx,count + 1])
    print(minCount)

bfs()