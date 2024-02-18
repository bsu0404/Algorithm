from collections import deque
import sys
mtx = [list(map(int,input().split())) for _ in range(19)]
visited = [[[0,0,0,0]for _ in range(20)] for _ in range(20)]
# [ 우하향, 우상향, 가로, 세로]

MOVE = [[1,1],[1,-1],[0,1],[1,0]]
# [ 우하향, 우상향, 가로, 세로]
def checkColor(i,j,p):
    color = mtx[i][j]
    cnt=1
    while True: #개수
        nx,ny = i+MOVE[p][0]*cnt,j+MOVE[p][1]*cnt
        if not (0 <= nx < 19  and 0 <= ny < 19):
            break
        if visited[nx][ny][p] !=0:
            break
        if mtx[nx][ny] != color:
            break
        visited[nx][ny][p] += 1
        cnt+=1
    return cnt

for i in range(19):
    for j in range(19):
        color = mtx[i][j]
        if color!=0 :
            for p in range(4):
                cnt =  checkColor(i,j,p)
                if cnt == 5:
                    ans = [[i,j],[i+4,j-4],[i,j],[i,j]]
                    print(color)
                    print(ans[p][0]+1, ans[p][1]+1)
                    sys.exit()

print(0)