M,N=map(int,input().split())

mtx = [list(input()) for _ in range(M)]

newMtx = [[["X"] * 4 for _ in range(N)] for _ in range(M)]



for i in range(1,M-1):
    for j in range(1,N-1):
        up,down,left,right=mtx[i-1][j], mtx[i+1][j],mtx[i][j-1], mtx[i][j+1]
        if mtx[i][j] == ".":
            if up == "X" :
                newMtx[i-1][j][0] = "O"
            if down=="X" :
                newMtx[i+1][j][1] = "O"
            if left=="X" :
                newMtx[i][j-1][2] = "O"
            if right=="X" :
                newMtx[i][j+1][3] = "O"

cnt = 0
#위
for i in range(M):
    current = 0
    for j in range(N):
        if newMtx[i][j][0] == "O" :
            current += 1
        if newMtx[i][j][0] != "O":
            cnt += (current//2)
            current = 0
#아래
for i in range(M):
    current = 0
    for j in range(N):
        if newMtx[i][j][1] == "O" :
            current += 1
        if newMtx[i][j][1] != "O":
            cnt += (current//2)
            current = 0


for i in range(N):
    current = 0
    for j in range(M):
        if newMtx[j][i][2] == "O" :
            current += 1
        if newMtx[j][i][2] != "O":
            cnt += (current//2)
            current = 0

for i in range(N):
    current = 0
    for j in range(M):
        if newMtx[j][i][3] == "O" :
            current += 1
        if newMtx[j][i][3] != "O":
            cnt += (current//2)
            current = 0
                
print(cnt)