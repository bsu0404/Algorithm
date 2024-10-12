
from collections import deque
import sys
input = sys.stdin.readline

def topology_sort(W):
    queue = deque()
    result = []
    dp = [0] * (N+1)

    # 진입차수 0인 노드 큐에 삽입
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = times[i-1]
            
    while queue:
        node = queue.popleft()
        result.append(node)

        for v in adjList[node]:
            indegree[v] -= 1
            dp[v] = max(dp[v],dp[node] + times[v-1])
            if indegree[v] == 0:
                queue.append(v)
    
    print(dp[W])


T = int(input())

for _ in range(T):
    N, K = map(int, input().split()) # 건물 수, 규칙 수
    adjList = [[] for _ in range(N+1)] 
    indegree = [0] * (N+1)

    times = list(map(int,input().split())) # 건물 짓는데 걸리는 시간

    for i in range(K): # 규칙
        v1, v2 = map(int, input().split())
        adjList[v1].append(v2)
        indegree[v2] += 1

    W = int(input())

    topology_sort(W)

