
MOVE = [[-1,0],[0,-1],[1,0],[0,1]]
N, M = map(int,input().split())
x, y, d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

arr[x][y] = 2
ans = 2

if d % 2 == 1:
    d = (d + 2) % 4
d = (d + 1) % 4


while True:
    tmp = 0
    
    for i in range(4):
        move = MOVE[(d + i) % 4]
        xx, yy = x + move[0], y + move[1],
        if (0  <= xx < N) and (0 <= yy < M ):
            if arr[xx][yy] == 0:
                x, y  = xx, yy
                ans += 1
                arr[xx][yy] = ans
                d = (d + i + 1) % 4
                tmp = 1
                break
  
    if tmp == 0:
    
        x += MOVE[(d + 1) % 4][0]
        y += MOVE[(d + 1) % 4][1]
        if not (0 <= x < N) or not (0 <= y < M) or arr[x][y] == 1:
            break

print(ans-1)

