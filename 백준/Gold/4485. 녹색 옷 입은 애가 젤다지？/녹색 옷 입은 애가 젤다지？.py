# function

import heapq
import sys

MOVE = [[1, 0], [-1 ,0], [0, 1], [0, -1]] 
INF = sys.maxsize


def dijkstra():
    que = []
    heapq.heappush(que, (mtx[0][0],[0,0]))

    while que :
        c, location = heapq.heappop(que)
        x = location[0]
        y = location[1]
        if cost[x][y] < c:
            continue

        for xx, yy in MOVE:
            nx, ny = x + xx, y + yy
            if not ((0 <= nx < N) and (0 <= ny < N)):
                continue
            w = cost[x][y] + mtx[nx][ny]
            if (0 <= nx < N) and (0 <= ny < N) and w < cost[nx][ny]:
                cost[nx][ny] = w
                heapq.heappush(que, (w,[nx,ny]))
             

# main

N = int(input())
num = 1
while N != 0:
    mtx = []
    cost = [[INF] * N for _ in range(N)]
    for i in range(N):
        tmp = list(map(int, input().split()))
        mtx.append(tmp)
    cost[0][0] = mtx[0][0]
    dijkstra()

    print("Problem %d: %d" %(num, cost[N-1][N-1]))
    N = int(input())
    num += 1

    