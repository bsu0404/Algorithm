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
                prev[v] = x
                heapq.heappush(que, (w,v))
            
# main
N = int(input())
M = int(input())

adjList = [[] for _ in range(N + 1)]
dist = [INF] * (N+1)
prev = [-1] * (N+1)

for _ in range(M):
    s, e, w = map(int, input().split())
    adjList[s].append((e, w))

s, e = map(int,input().split())
dist[s] = 0

dijkstra(s)

path = [e]
v = e
while v != s:
    path.append(prev[v])
    v = prev[v]

print(dist[e])
print(len(path))
print(*path[::-1],sep = " ")