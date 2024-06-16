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
N, M = map(int,input().split())

adjList = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    adjList[s].append((e, w))
    adjList[e].append((s, w))

v1, v2 = map(int,input().split())

# v1 -> v2
dist = [INF] * (N+1)
dist[v1] = 0
dijkstra(v1)
d = dist[v2]

# 1 -> v1 or v2
dist = [INF] * (N+1)
dist[1] = 0
dijkstra(1)
s1, s2 = dist[v1], dist[v2]

# N -> v1 or v2
dist = [INF] * (N+1)
dist[N] = 0
dijkstra(N)
e1, e2 = dist[v1], dist[v2]

ans = min(d + s1 + e2, d + s2 + e1, 2 * d + s1 + e1, 2 * d + s2 + e2 )
print(ans if ans < INF else "-1")