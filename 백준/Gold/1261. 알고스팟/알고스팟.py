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
            if not ((0 <= nx < N) and (0 <= ny < M)):
                continue
            w = cost[x][y] + mtx[nx][ny]
            if (0 <= nx < N) and (0 <= ny < M) and w < cost[nx][ny]:
                cost[nx][ny] = w
                heapq.heappush(que, (w,[nx,ny]))
             

# main

M, N = map(int, input().split())
num = 1
mtx = []
cost = [[INF] * M for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input()))
    mtx.append(tmp)
cost[0][0] = mtx[0][0]
dijkstra()
print(cost[N-1][M-1])