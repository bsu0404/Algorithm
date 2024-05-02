from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

# function
def dfs(index, p):
    p.append(index)
    if len(tree[index][0])== 0:
        return 
    dfs(tree[index][0][0], p) 

def getCommonParent(p1, p2):
    minLen = min(len(p1), len(p2))
    while len(p1) != minLen:
        p1.popleft()
    while len(p2) != minLen:
        p2.popleft()
    v1 = p1.popleft()
    v2 = p2.popleft()
    while v1 != v2:
        v1 = p1.popleft()
        v2 = p2.popleft()
    print(v1)

# main
T = int(input())
for _ in range(T):
    N = int(input())
    tree=[[[] for _ in range(2)] for _ in range(N+1)]
    for _ in range(N - 1):
        # tree[node][0]: 부모 / tree[node][1]: 자식
        p, c = map(int, input().split())
        tree[c][0].append(p)
        tree[p][1].append(c)
    v1, v2 = map(int,input().split())
    p1 = deque()
    p2 = deque()
    dfs(v1, p1)
    dfs(v2, p2)
    getCommonParent(p1, p2)


