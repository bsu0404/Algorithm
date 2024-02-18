from collections import deque
import sys

N,L,R = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

MOVE = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(visited,x,y) :
    needVisit = []
    needVisit.append([x,y])
    visited[x][y]=1
    i=0
    sum = 0


    while(True):
        x,y = needVisit[i]
        num = graph[x][y]
        sum+=num

        for move in MOVE:
            xx, yy = move
            nx, ny = x + xx, y +yy
            if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny] == 0) :
                if L<=abs(graph[nx][ny]-num)<=R:
                    visited[nx][ny] = 1
                    needVisit.append([nx, ny])       
                
        i+=1
        if(len(needVisit)==i):
            break
    return needVisit , sum 


count = 0


while(True):
    visited = [[0] * N for _ in range(N)]
    change =0

    for i in range(N) :
        for j in range(N) :
            if (visited[i][j] == 0) :
                visitednode, sum = bfs(visited,i,j)
                length = len(visitednode)               
                if (length>1):
                    change+=1
                    for x,y in visitednode:
                        graph[x][y] = int(sum/length)
    if change == 0:
        break
    count += 1
    


print(count)
        