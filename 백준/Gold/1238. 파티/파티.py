import sys
import heapq
input = sys.stdin.readline

V,E,X=map(int,input().split())
adjList = [[] for _ in range(V + 1) ]
INF = sys.maxsize

for _ in range(E):
    s,e,w = map(int,input().split())
    adjList[s].append((e,w))

def dijkstra(s):
    que = []
    heapq.heappush(que, (0, s))
    dist = [INF] * (V+1)
    dist[s] = 0

    while que:
        cost, x = heapq.heappop(que)
        #if x == X:
        #  break
        if dist[x] < cost:
            continue
        for v, w in adjList[x]:
            w += cost
            if w < dist[v]:
                dist[v] = w
                heapq.heappush(que, (w, v))
    return dist

maxDist =[0]*(V+1)
for i in range(1,V+1):
    dist = dijkstra(i)
    maxDist[i] += dist[X]
    if i == X:
        for j in range(1,V+1):
            maxDist[j] += dist[j]

maxValue = 0
for i in range(1,V+1):
    maxValue = max(maxValue,maxDist[i])

print(maxValue)
