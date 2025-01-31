from collections import deque

# function
def bfs(i,j):
    queue = deque()
    queue.append((i, j))
    visited.add((i,j))
    
    while queue:
        x,y = queue.popleft()
        if abs(x-endX) + abs(y-endY) <= 1000:
            visited.add((x,y))
            return True

        for xx, yy in mart:
            if (xx,yy) not in visited and abs(x-xx) + abs(y-yy) <= 1000:
                queue.append((xx, yy))
                visited.add((xx,yy))

    return False

# main

T = int(input())

for _ in range(T):
    N = int(input())
    visited = set()

    startX,startY = map(int, input().split())
    mart = set()
    for _ in range(N):
        x, y = map(int, input().split())
        mart.add((x, y))
    endX, endY = map(int, input().split())

    ans = bfs(startX,startY)


    if ans:
        print("happy")
    else:
        print("sad")