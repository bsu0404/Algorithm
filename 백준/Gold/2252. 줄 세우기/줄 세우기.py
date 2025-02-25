from collections import deque
import sys
input = sys.stdin.readline


def topology_sort():
    queue = deque()
    result = []

    # 진입차수 0인 노드 큐에 삽입
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        node = queue.popleft()
        result.append(node)

        for v in adjList[node]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    print(*result)



N, K = map(int, input().split()) 
adjList = [[] for _ in range(N+1)] 
indegree = [0] * (N+1)


for i in range(K): # 규칙
    v1, v2 = map(int, input().split())
    adjList[v1].append(v2)
    indegree[v2] += 1


topology_sort()

