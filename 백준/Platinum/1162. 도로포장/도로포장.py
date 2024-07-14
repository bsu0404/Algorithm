import sys
input = sys.stdin.readline
import heapq
INF = float('inf')

N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]

distance = [[INF] * (K + 1) for _ in range(N + 1)]

for i in range(M) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start):
    queue = []
    cnt = 0
    heapq.heappush(queue, (0, start, cnt))
    for i in range(K + 1) :
        distance[start][i] = 0

    while queue :
        dist, minindex, pcnt = heapq.heappop(queue)

        if distance[minindex][pcnt] < dist :
            continue

        if pcnt + 1 <= K :
            for g in graph[minindex] :
                if distance[g[0]][pcnt + 1] > dist :
                    distance[g[0]][pcnt + 1] = dist
                    heapq.heappush(queue, (dist, g[0], pcnt + 1))

        for g in graph[minindex] :
            if dist + g[1] < distance[g[0]][pcnt] :
                distance[g[0]][pcnt] = dist + g[1]
                heapq.heappush(queue, (dist + g[1], g[0], pcnt))

    return(min(distance[N]))

print(dijkstra(1))
#print(distance)