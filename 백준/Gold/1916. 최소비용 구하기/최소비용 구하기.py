#function

import heapq
import sys

INF = sys.maxsize
input = sys.stdin.readline


def dijkstra(s):
    que = []
    heapq.heappush(que, (0,s))

    while que :
        cost, x = heapq.heappop(que)
        if dist[x] < cost:
            continue

        for v, w in adjList[x]:
            w += cost
            if w < dist[v]:
                dist[v] = w
                heapq.heappush(que, (w,v))
            
# main
N = int(input())
M = int(input())

adjList = [[] for _ in range(N + 1)]
dist = [INF] * (N+1)

for _ in range(M):
    s, e, w = map(int, input().split())
    adjList[s].append((e, w))

s, e = map(int,input().split())
dist[s] = 0

dijkstra(s)
print(dist[e])