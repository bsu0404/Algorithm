import sys
input = sys.stdin.readline

N, M = map(int,input().split())
edges = []
INF = sys.maxsize
dist = [INF] * (N+1)


for _ in range(M):
    s,e,w = map(int,input().split())
    edges.append((s,e,w))

def bellmanFord(s):
    dist[s] = 0

    for i in range(N):
        for j in range(M): # 모든 간선
            s = edges[j][0]
            e = edges[j][1]
            cost = edges[j][2]

            if dist[s] != INF and dist[e] > dist[s] + cost:
                dist[e] = dist[s] + cost

                if i == N - 1: 
                # N번째에도 값이 갱신된다면 음수 순환 존재
                    return True
    return False


cycle = bellmanFord(1)
if cycle:
    print("-1")
else:
    for i in range(2,N+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
