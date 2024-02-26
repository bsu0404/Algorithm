import sys
import heapq
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
INF = sys.maxsize

adjList = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    adjList[s].append((e, w))
def dijkstra(s):
    que = []
    heapq.heappush(que, (0, s))
    dist = [INF] * (V+1)
    dist[s] = 0

    while que:
        cost, x = heapq.heappop(que)
        if dist[x] < cost:
            continue
        for v, w in adjList[x]:
            w += cost
            if w < dist[v]:
                dist[v] = w
                heapq.heappush(que, (w, v))
    return dist

dist = dijkstra(K)
for i in range(1, V + 1):
    if dist[i] < INF:
        print(dist[i])
    else:
        print("INF")
