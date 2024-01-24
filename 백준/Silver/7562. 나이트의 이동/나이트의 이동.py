from collections import deque

MOVE = [[-2,-1],[-1,-2],[1,-2],[2,-1],[-2,1],[-1,2],[1,2],[2,1]]

def bfs(start,end, l):
    x,y =start
    a,b = end
    minCount = float("inf")
    needVisit = deque()
    visited = [[0] * l for _ in range(l)]

    needVisit.append([x, y, 0])
    visited[x][y] = 1
    
    while len(needVisit)>0:
        x, y, count = needVisit.popleft()

        if x == a and y == b:
            minCount = min(count, minCount)

        for move in MOVE:
            xx, yy = move
            nx, ny = x + xx, y + yy           
            if (0 <= nx < l) and (0 <= ny < l) and (visited[nx][ny] == 0):
                visited[nx][ny] = 1
                needVisit.append([nx, ny, count + 1])
    print(minCount)

for _ in range(int(input())) :
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    bfs(start,end,l)
    